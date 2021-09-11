# 웹소켓을 통한 실시간 인터랙션 구현

## websocket

웹 서버와 웹 브라우저(클라이언트)간의 실시간 양방향 통신 환경을 제공해 주는 실시간 통신 기술

## koa.js

- Node.js 에서 가장 인기있던 웹 프레임워크인 Express.js 의 개발팀이, Koa 라는 웹프레임워크를 새로 만듬
- Express 와의 큰 차이는, Koa 는 훨씬 가볍고, Node.js v7 의 async/await 기능을 아주 편하게 사용 할 수 있음

```bash
$ npm install koa
```

```javascript
const Koa = require("koa");
const app = new Koa();

app.use(async (ctx) => {
  ctx.body = "Hello World";
});

app.listen(3000);
```

## tailwind CSS

- Utility-First 를 지향하는 CSS 프레임워크
- 사전에 정의되어 있는 유틸리티 클래스를 사용하여 간단하게 스타일을 적용

```bash
$ npm install tailwindcss
```

```html
<link
  href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css"
  rel="stylesheet"
/>
```

## koa-websocket

```bash
$ npm install koa-websocket
```

```javascript
const Koa = require("koa"),
  route = require("koa-route"),
  websockify = require("koa-websocket");

const app = websockify(new Koa());

app.ws.use(function (ctx, next) {
  return next(ctx);
});

// Using routes
app.ws.use(
  route.all("/test/:id", function (ctx) {
    ctx.websocket.send("Hello World");
    ctx.websocket.on("message", function (message) {
      console.log(message);
    });
  })
);

app.listen(3000);
```

## 실시간 인터랙션 구현

- **유니캐스트** : 송신 노드 하나가 수신 노드 하나에 데이터를 전송하는 일대일 방식
- **브로드캐스트** : 같은 네트워크에 있는 모든 장비들에게 보내는 통신

```javascript
// src/main.js

const Koa = require("koa");
const Pug = require("koa-pug");
const path = require("path");
const route = require("koa-route");
const serve = require("koa-static");
const websockify = require("koa-websocket");
const mount = require("koa-mount");
const mongoClient = require("./mongo");

const app = websockify(new Koa());

new Pug({
  viewPath: path.resolve(__dirname, "./views"),
  app,
});

app.use(mount("/public", serve("src/public")));

app.use(async (ctx) => {
  await ctx.render("main");
});

app.ws.use(
  route.all("/ws", (ctx) => {
    ctx.websocket.on("message", (data) => {
      if (typeof data !== "string") {
        return;
      }

      const { message, nickname } = JSON.parse(data);

      // 유니캐스트 상태이므로 브로드캐스트 상태로 변환이 필요
      const { server } = app.ws;

      if (!server) {
        return;
      }

      // 브로드캐스트 변환 - 모든 client에 전송
      server.clients.forEach((client) => {
        client.send(
          JSON.stringify({
            message,
            nickname,
          })
        );
      });
    });
  })
);

app.listen(3000);
```

- `IIFE` : 즉시 실행 함수 표현, 브라우저 console 창에서 socket 이 노출되는 부분을 막기 위해 활용

```javascript
// src/public/client.js

// IIFE
(() => {
  const socket = new WebSocket(`ws://${window.location.host}/ws`);
  const formEl = document.getElementById("form");
  const chatsEl = document.getElementById("chats");
  const inputEl = document.getElementById("input");

  if (!formEl || !inputEl || !chatsEl) {
    throw new Error("Init failed!");
  }

  const chats = [];

  const adjectives = ["멋진", "훌륭한", "친절한", "새침한"];
  const animals = ["물범", "사자", "사슴", "돌고래", "독수리"];

  function pickRandom(array) {
    const randomIdx = Math.floor(Math.random() * array.length);
    const result = array[randomIdx];
    if (!result) {
      throw new Error("array length is 0.");
    }
    return result;
  }

  const myNickname = `${pickRandom(adjectives)} ${pickRandom(animals)}`;

  formEl.addEventListener("submit", (event) => {
    // form 요청하면서 갱신 막기
    event.preventDefault();
    socket.send(
      JSON.stringify({
        nickname: myNickname,
        message: inputEl.value,
      })
    );
    inputEl.value = "";
  });

  socket.addEventListener("message", (event) => {
    chats.push(JSON.parse(event.data));

    chatsEl.innerHTML = "";

    chats.forEach(({ nickname, message }) => {
      const div = document.createElement("div");
      div.innerText = `${nickname}: ${message}`;
      chatsEl.appendChild(div);
    });
  });
})();
```

## MongoDB 에 인터랙션 정보 저장

```javascript
// src/mongo.js

const { MongoClient } = require("mongodb");

const uri =
  "mongodb+srv://<username>:<password>@cluster0.zr1pn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

module.exports = client;
```

```javascript
// src/main.js

const Koa = require("koa");
const Pug = require("koa-pug");
const path = require("path");
const route = require("koa-route");
const serve = require("koa-static");
const websockify = require("koa-websocket");
const mount = require("koa-mount");
const mongoClient = require("./mongo");

const app = websockify(new Koa());

new Pug({
  viewPath: path.resolve(__dirname, "./views"),
  app,
});

app.use(mount("/public", serve("src/public")));

app.use(async (ctx) => {
  await ctx.render("main");
});

const _client = mongoClient.connect();

async function getChatsCollection() {
  const client = await _client;
  return client.db("chat").collection("chats");
}

app.ws.use(
  route.all("/ws", async (ctx) => {
    const chatsCollection = await getChatsCollection();
    // createdAt 오름차순으로 정렬하여 chat 데이터 가져오기
    const chatsCursor = chatsCollection.find(
      {},
      {
        sort: {
          createdAt: 1,
        },
      }
    );

    const chats = await chatsCursor.toArray();
    ctx.websocket.send(
      JSON.stringify({
        type: "sync",
        payload: {
          chats,
        },
      })
    );

    ctx.websocket.on("message", async (data) => {
      if (typeof data !== "string") {
        return;
      }

      const chat = JSON.parse(data);

      chatsCollection.insertOne({
        ...chat,
        createdAt: new Date(),
      });

      const { nickname, message } = chat;

      // 유니캐스트 상태이므로 브로드캐스트 상태로 변환이 필요
      const { server } = app.ws;

      if (!server) {
        return;
      }

      // 브로드캐스트 변환 - 모든 client에 전송
      server.clients.forEach((client) => {
        client.send(
          JSON.stringify({
            type: "chat",
            payload: {
              message,
              nickname,
            },
          })
        );
      });
    });
  })
);

app.listen(3000);
```

```javascript
// src/public/client.js

// IIFE
(() => {
  const socket = new WebSocket(`ws://${window.location.host}/ws`);
  const formEl = document.getElementById("form");
  const chatsEl = document.getElementById("chats");
  const inputEl = document.getElementById("input");

  if (!formEl || !inputEl || !chatsEl) {
    throw new Error("Init failed!");
  }

  const chats = [];

  const adjectives = ["멋진", "훌륭한", "친절한", "새침한"];
  const animals = ["물범", "사자", "사슴", "돌고래", "독수리"];

  function pickRandom(array) {
    const randomIdx = Math.floor(Math.random() * array.length);
    const result = array[randomIdx];
    if (!result) {
      throw new Error("array length is 0.");
    }
    return result;
  }

  const myNickname = `${pickRandom(adjectives)} ${pickRandom(animals)}`;

  formEl.addEventListener("submit", (event) => {
    // form 요청하면서 갱신 막기
    event.preventDefault();
    socket.send(
      JSON.stringify({
        nickname: myNickname,
        message: inputEl.value,
      })
    );
    inputEl.value = "";
  });

  const drawChats = () => {
    chatsEl.innerHTML = "";
    chats.forEach(({ nickname, message }) => {
      const div = document.createElement("div");
      div.innerText = `${nickname}: ${message}`;
      chatsEl.appendChild(div);
    });
  };

  socket.addEventListener("message", (event) => {
    const { type, payload } = JSON.parse(event.data);

    if (type === "sync") {
      const { chats: syncedChats } = payload;
      chats.push(...syncedChats);
    } else if (type === "chat") {
      const chat = payload;
      chats.push(chat);
    }

    drawChats();
  });
})();
```
