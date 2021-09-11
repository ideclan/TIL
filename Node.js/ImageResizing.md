# 이미지 리사이징 서버

키워드로 검색해서 나온 이미지를 원하는 사이즈로 리사이징해서 돌려주는 서버

## 외부 소스에서 원하는 이미지 가져오기

### Unsplash

- 저작권 걱정없이 무료로 사진이나 이미지를 다운받아 사용이 가능
- API 를 지원

```bash
$ npm install unsplash-js node-fetch
```

- 요청한 키워드에 대한 unsplash API 첫번째 검색결과 이미지를 저장 후 반환

```javascript
/*
"node-fetch": "^2.6.1",
"unsplash-js": "^7.0.11"
*/

const fs = require("fs");
const path = require("path");
const http = require("http");
const { createApi } = require("unsplash-js");
const { default: fetch } = require("node-fetch");
const { pipeline } = require("stream");
const { promisify } = require("util");

const unsplash = createApi({
  accessKey: "MY_ACCESS_KEY",
  fetch,
});

async function searchImage(query) {
  // unsplash 이미지 검색 API
  const result = await unsplash.search.getPhotos({ query });

  if (!result.response) {
    throw Error("Failed to search image.");
  }

  // 해당 이미지 1개
  const image = result.response.results[0];

  if (!image) {
    throw new Error("No image found.");
  }

  return {
    description: image.description || image.alt_description,
    url: image.urls.regular,
  };
}

// 이미지를 Unsplash 에서 검색하거나, 이미 있다면 캐시된 이미지를 반환
async function getCachedImageOrSearchedImage(query) {
  const imageFilePath = path.resolve(__dirname, `../images/${query}`);

  // 이미 파일이 존재한다면
  if (fs.existsSync(imageFilePath)) {
    return fs.createReadStream(imageFilePath);
  }

  const result = await searchImage(query);
  const resp = await fetch(result.url);

  // 이미지 저장
  await promisify(pipeline)(resp.body, fs.createWriteStream(imageFilePath));

  // 저장한 이미지를 반환
  return fs.createReadStream(imageFilePath);
}

function convertURL(url) {
  // url 에 포함된 '/' 제외
  return url.slice(1);
}

const server = http.createServer((req, res) => {
  async function main() {
    if (!req.url) {
      res.statusCode = 400;
      res.end("Needs URL.");
      return;
    }

    const query = convertURL(req.url);
    try {
      const stream = await getCachedImageOrSearchedImage(query);
      stream.pipe(res);
    } catch {
      res.statusCode = 400;
      res.end();
    }
  }

  main();
});

const PORT = 3000;

server.listen(PORT, () => {
  console.log("The server is listening at port", PORT);
});
```

## 이미지 리사이징

### sharp

```bash
$ npn install sharp
```

```javascript
const sharp = require("sharp");

// 이미지를 Unsplash 에서 검색하거나, 이미 있다면 캐시된 이미지를 반환
async function getCachedImageOrSearchedImage(query) {
  const imageFilePath = path.resolve(__dirname, `../images/${query}`);

  // 이미 파일이 존재한다면
  if (fs.existsSync(imageFilePath)) {
    return fs.createReadStream(imageFilePath);
  }

  const result = await searchImage(query);
  const resp = await fetch(result.url);

  // 이미지 저장
  await promisify(pipeline)(resp.body, fs.createWriteStream(imageFilePath));

  // 저장한 이미지를 반환
  return fs.createReadStream(imageFilePath);
}

function convertURLToImageInfo(url) {
  const urlObj = new URL(url, "http://localhost:3000");

  function getSearchParam(name, defaultValue) {
    const str = urlObj.searchParams.get(name);
    return str ? parseInt(str, 10) : defaultValue;
  }

  const width = getSearchParam("width", 400);
  const height = getSearchParam("height", 400);

  return {
    // url 에 포함된 '/' 제외
    query: urlObj.pathname.slice(1),
    width,
    height,
  };
}

const server = http.createServer((req, res) => {
  async function main() {
    if (!req.url) {
      res.statusCode = 400;
      res.end("Needs URL.");
      return;
    }

    const { query, width, height } = convertURLToImageInfo(req.url);
    try {
      const stream = await getCachedImageOrSearchedImage(query);

      await promisify(pipeline)(
        stream,
        sharp()
          .resize(width, height, {
            fit: "cover", // 옵션
          })
          .png(),
        res
      );
    } catch {
      res.statusCode = 400;
      res.end();
    }
  }

  main();
});

const PORT = 3000;

server.listen(PORT, () => {
  console.log("The server is listening at port", PORT);
});
```

### image-size

- 이미지 사이즈 추출

```bash
$ npm install image-size
```
