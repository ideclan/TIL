# Vue.js

## Vue CLI로 프로젝트 생성

```bash
$ vue create vue-todo

# default (babel, eslint) 기본값
# Manually select features 여러가지 기능을 선택하여 구성이 가능

$ cd vue-todo
$ npm run serve
```

## 컴포넌트 생성 및 등록

- my-project/src/components 경로에 TodoHeader.vue 생성

```javascript
<template>
  <div>
    header
  </div>
<template>

<script>
export default {

};
</script>

<style>

</style>
```

- my-project/src/App.vue
  - Template root 는 하나의 Element 만 허용 ( div tag 1개 )

```javascript
<template>
  <div id="app">
    <TodoHeader></TodoHeader>
  </div>
</template>

<script>
import TodoHeader from "./components/TodoHeader.vue";

export default {
  // 컴포넌트 태그명: 컴포넌트 내용
  TodoHeader: TodoHeader,
};
</script>

<style>

</style>
```

## Favicon, Icon, Font, 반응형 태그 설정

index.html에 적용

- Favicon : [https://www.favicon-generator.org/](https://www.favicon-generator.org/)

```html
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<link rel="icon" href="/favicon.ico" type="image/x-icon" />
```

- Fontawesome Icon

```html
<link
  rel="stylesheet"
  href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
  integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p"
  crossorigin="anonymous"
/>
```

- Google Font Ubuntu

```html
<link
  rel="stylesheet"
  type="text/css"
  href="//fonts.googleapis.com/css?family=Ubuntu"
/>
```

- 반응형 태그 설정 (모바일)

```html
<meta name="viewport" content="width=device-width,initial-scale=1.0" />
```

## Header 컴포넌트 구현

TodoHeader.vue

- `scoped` : 해당 컴포넌트 안에서만 적용하는 설정
- 알아두면 상식
  - font-weight은 글자 굵기
  - margin에서 px단위가 아닌 rem을 사용하면 글자 굵기에 비율이 정해짐

```javascript
<template>
  <header>
    <h1>TODO it!</h1>
  </header>
</template>

<style scoped>
h1 {
  color: #2f3b52;
  font-weight: 900;
  margin: 2.5rem 0 1.5rem;
}
</style>
```

App.vue

```javascript
<template>
  <div id="app">
    <TodoHeader></TodoHeader>
    <TodoInput></TodoInput>
    <TodoList></TodoList>
    <TodoFooter></TodoFooter>
  </div>
</template>

<script>
import TodoHeader from "./components/TodoHeader.vue";
import TodoInput from "./components/TodoInput.vue";
import TodoList from "./components/TodoList.vue";
import TodoFooter from "./components/TodoFooter.vue";

export default {
  components: {
    // 컴포넌트 태그명: 컴포넌트 내용
    TodoHeader: TodoHeader,
    TodoInput: TodoInput,
    TodoList: TodoList,
    TodoFooter: TodoFooter,
  },
};
</script>

<style>
body {
  text-align: center;
  background-color: #f6f6f6;
}
input {
  border-style: groove;
  width: 200px;
}
button {
  border-style: groove;
}
.shadow {
  box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03);
}
</style>
```

### 컴포넌트 저장 기능 구현

TodoInput.vue

- `v-model` : Input에 입력된 텍스트 값을 동적으로 Vue 인스턴스와 연결하는 역할
- `v-on:click` : 클릭했을 때 호출되는 method 정의
- `v-on:keyup.enter` : enter를 눌렀을 때 호출되는 method 정의
- Fontawesome Icon을 사용하여 `<span><i>`로 버튼처럼 만들 수 있음
- 외부 App.vue에서 정의한 style을 사용할 수 있음
- 아직 DB를 사용하지 않으므로 localStorage API를 사용하여 저장된 key, value는 크롬 웹 브라우저 > 개발자 도구 > Application > Storage > Local Storage > localhost:8080에서 확인 가능

```javascript
<template>
  <div class="inputBox shadow">
    <input type="text" v-model="newTodoItem" v-on:keyup.enter="addTodo" />
    <!-- <button v-on:click="addTodo">add</button> -->
    <span class="addContainer" v-on:click="addTodo">
      <i class="fas fa-plus addBtn"></i>
    </span>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      newTodoItem: "",
    };
  },
  methods: {
    addTodo: function () {
      // 저장하는 로직
      localStorage.setItem(this.newTodoItem, this.newTodoItem);
      this.clearInput();
    },
    clearInput: function () {
      this.newTodoItem = "";
    },
  },
};
</script>

<style scoped>
input:focus {
  outline: none;
}
.inputBox {
  background: white;
  height: 50px;
  line-height: 50px;
  border-radius: 5px;
}
.inputBox input {
  border-style: none;
  font-size: 0.9rem;
}
.addContainer {
  float: right;
  background: linear-gradient(to right, #6478fb, #8763fb);
  display: block;
  width: 3rem;
  border-radius: 0 5px 5px 0;
}
.addBtn {
  color: white;
  vertical-align: middle;
}
</style>
```

### 컴포넌트 표시, 삭제 기능 구현

TodoList.vue

- `created` : 인스턴스가 생성되면서 호출되는 라이프 사이클 훅(생성되는 시점에 호출)
- `this` : 같은 인스턴스를 가르키기 때문에 this로 data의 todoItems 값에 접근이 가능
- `v-for` : todoItems 배열 안에서 todoItem 개수만큼 반복 (`v-for`를 사용할 때는 `v-bind:key` 사용, index는 꼭 사용하지 않아도 됨)
- 알아두면 상식 : JS API `splice( )` 해당 배열에서 값을 지우고 새로운 배열을 반환 ≠ `slice( )`

  **TodoInput.vue** 에서 `JSON.stringify( )`로 현재는 데이터가 String 타입이므로 객체로 변환하려면 `JSON.parse( )` 사용

- `v-bind:class="클래스명: 조건"` : 조건이 false면 해당 클래스가 적용되지 않음

```javascript
<template>
  <div>
    <ul>
      <li v-for="(todoItem, index) in todoItems" v-bind:key="todoItem.item" class="shadow">
        <i
          class="checkBtn fas fa-check"
          v-bind:class="{checkBtnCompleted: todoItem.completed}"
          v-on:click="toggleComplete(todoItem, index)"
        ></i>
        <span v-bind:class="{textCompleted: todoItem.completed}">{{ todoItem.item }}</span>
        <span class="removeBtn" v-on:click="removeTodo(todoItem, index)">
          <i class="fas fa-trash-alt"></i>
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      todoItems: [],
    };
  },
  methods: {
    removeTodo: function (todoItem, index) {
      localStorage.removeItem(todoItem);
      this.todoItems.splice(index, 1);
    },
    toggleComplete: function (todoItem, index) {
      // true로 변경
      todoItem.completed = !todoItem.completed;
      // 로컬 스토리지 갱신
      localStorage.removeItem(todoItem.item);
      localStorage.setItem(todoItem.item, JSON.stringify(todoItem));
    },
  },
  created: function () {
    if (localStorage.length > 0) {
      for (var i = 0; i < localStorage.length; i++) {
        // 로컬 스토리지 기존에 저장된 데이터에 대한 것으로 if문 조건은 무시해도 됨
        if (
          localStorage.key(i) !== "loglevel:webpack-dev-server" &&
          localStorage.key(i) !== "user"
        ) {
          this.todoItems.push(
            JSON.parse(localStorage.getItem(localStorage.key(i)))
          );
        }
      }
    }
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0;
  margin-top: 0;
  text-align: left;
}
li {
  display: flex;
  min-height: 50px;
  height: 50px;
  line-height: 50px;
  margin: 0.5rem 0;
  padding: 0 0.9rem;
  background: white;
  border-radius: 5px;
}
.removeBtn {
  margin-left: auto;
  color: #de4343;
}
.checkBtn {
  line-height: 45px;
  color: #62acde;
  margin-right: 5px;
}
.checkBtnCompleted {
  color: #b3adad;
}
.textCompleted {
  text-decoration: line-through;
  color: #b3adad;
}
</style>
```

TodoInput.vue > addTodo 수정

- 알아두면 상식 : `JSON.stringify( )` JS 객체를 String으로 변환

```javascript
methods: {
    addTodo: function () {
      // 해당 값이 있을 때
      if (this.newTodoItem !== "") {
        var obj = { completed: false, item: this.newTodoItem };
        localStorage.setItem(this.newTodoItem, JSON.stringify(obj));
        this.clearInput();
      }
    },
    clearInput: function () {
      this.newTodoItem = "";
    },
  }
```

TodoFooter.vue

```javascript
<template>
  <div class="clearAllContainer">
    <span class="clearAllbtn" v-on:click="clearTodo">Clear All</span>
  </div>
</template>

<script>
export default {
  methods: {
    clearTodo: function () {
      localStorage.clear();
    },
  },
};
</script>

<style scoped>
.clearAllContainer {
  width: 8.5rem;
  height: 50px;
  line-height: 50px;
  background-color: white;
  border-radius: 5px;
  margin: 0 auto;
}
.clearAllbtn {
  color: #e20303;
  display: block;
}
</style>
```

## 현재 앱 구조의 문제점

- 로컬 스토리지에 저장 또는 삭제는 되지만 리스트가 바로 갱신이 되지 않음 (새로고침을 해야 갱신이 됨)
- 하나의 컴포넌트에서 이벤트가 발생하여 데이터 변경이 일어났을 때 **다른 컴포넌트에서는 인식을 하지 못함**

![스크린샷 2020-09-02 오후 9 09 13](https://user-images.githubusercontent.com/48443734/92322779-48670000-f06e-11ea-8680-b850b9fdadd9.png)

## 리팩토링

- 다음과 같은 구조인 방식인 **컨테이너 컴포넌트** 설계 기법으로 변경

  - App.vue(상위 컴포넌트)에서는 데이터를 조작하고 Propsdata를 내려줌
  - 나머지(하위 컴포넌트)에서는 UI 표현만 하고 이벤트를 올려줌

- `v-bind: 내려보낼 props 속성 이름="현재 위치의 컴포넌트 데이터"`
- `v-on: 하위 컴포넌트에서 발생시킨 이벤트 이름="현재 컴포넌트의 메서드 명"`
  - `this.$emit('이벤트 이름', 인자1, 인자2 ... )` 하위 컴포넌트에서 해당 이벤트 이름으로 이벤트를 발생시켜 상위 컴포넌트에 전송

![스크린샷 2020-09-02 오후 9 10 35](https://user-images.githubusercontent.com/48443734/92322783-4d2bb400-f06e-11ea-83a0-2e90b0a9866d.png)

App.vue

```javascript
<template>
  <div id="app">
    <TodoHeader></TodoHeader>
    <TodoInput v-on:addTodoItem="addOneItem"></TodoInput>
    <TodoList
      v-bind:propsdata="todoItems"
      v-on:removeItem="removeOneItem"
      v-on:toggleItem="toggleOneItem"
    >
    </TodoList>
    <TodoFooter v-on:clearAll="clearAllItems"></TodoFooter>
  </div>
</template>

<script>
import TodoHeader from './components/TodoHeader.vue';
import TodoInput from './components/TodoInput.vue';
import TodoList from './components/TodoList.vue';
import TodoFooter from './components/TodoFooter.vue';

export default {
  data: function() {
    return {
      todoItems: [],
    };
  },
  methods: {
    addOneItem: function(todoItem) {
      var obj = {completed: false, item: todoItem};
      localStorage.setItem(todoItem, JSON.stringify(obj));
      this.todoItems.push(obj);
    },
    removeOneItem: function(todoItem, index) {
      localStorage.removeItem(todoItem.item);
      this.todoItems.splice(index, 1);
    },
    toggleOneItem: function(todoItem, index) {
      this.todoItems[index].completed = !this.todoItems[index].completed;
      // 로컬 스토리지 갱신
      localStorage.removeItem(todoItem.item);
      localStorage.setItem(todoItem.item, JSON.stringify(todoItem));
    },
    clearAllItems: function() {
      localStorage.clear();
      this.todoItems = [];
    },
  },
  created: function() {
    if (localStorage.length > 0) {
      for (var i = 0; i < localStorage.length; i++) {
        if (
          localStorage.key(i) !== 'loglevel:webpack-dev-server' &&
          localStorage.key(i) !== 'user'
        ) {
          this.todoItems.push(
            JSON.parse(localStorage.getItem(localStorage.key(i)))
          );
        }
      }
    }
  },
  components: {
    // 컴포넌트 태그명: 컴포넌트 내용
    TodoHeader: TodoHeader,
    TodoInput: TodoInput,
    TodoList: TodoList,
    TodoFooter: TodoFooter,
  },
};
</script>
```

TodoList.vue

```javascript
<template>
  <div>
    <ul>
      <li v-for="(todoItem, index) in propsdata" v-bind:key="todoItem.item" class="shadow">
        <i
          class="checkBtn fas fa-check"
          v-bind:class="{checkBtnCompleted: todoItem.completed}"
          v-on:click="toggleComplete(todoItem, index)">
        </i>
        <span v-bind:class="{textCompleted: todoItem.completed}">
          {{
          todoItem.item
          }}
        </span>
        <span class="removeBtn" v-on:click="removeTodo(todoItem, index)">
          <i class="fas fa-trash-alt"></i>
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ["propsdata"],
  methods: {
    removeTodo: function (todoItem, index) {
      this.$emit("removeItem", todoItem, index);
    },
    toggleComplete: function (todoItem, index) {
      this.$emit("toggleItem", todoItem, index);
    },
  },
};
</script>
```

TodoInput.vue

```javascript
<template>
  <div class="inputBox shadow">
    <input type="text" v-model="newTodoItem" v-on:keyup.enter="addTodo" />
    <span class="addContainer" v-on:click="addTodo">
      <i class="fas fa-plus addBtn"></i>
    </span>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      newTodoItem: '',
    };
  },
  methods: {
    addTodo: function() {
      if (this.newTodoItem !== '') {
        this.$emit('addTodoItem', this.newTodoItem);
        this.clearInput();
      }
    },
    clearInput: function() {
      this.newTodoItem = '';
    },
  },
};
</script>
```

TodoFooter.vue

```javascript
<template>
  <div class="clearAllContainer">
    <span class="clearAllbtn" v-on:click="clearTodo">Clear All</span>
  </div>
</template>

<script>
export default {
  methods: {
    clearTodo: function() {
      this.$emit('clearAll');
    },
  },
};
</script>
```

## 모달 컴포넌트 등록

- [Vuejs.org Modal Components 예제](<[https://codesandbox.io/embed/github/vuejs/vuejs.org/tree/master/src/v2/examples/vue-20-modal-component?codemirror=1&hidedevtools=1&hidenavigation=1&theme=light](https://codesandbox.io/embed/github/vuejs/vuejs.org/tree/master/src/v2/examples/vue-20-modal-component?codemirror=1&hidedevtools=1&hidenavigation=1&theme=light)>)
- 모달 컴포넌트는 **재사용 할 수 있도록 모듈화** 하는 것을 추천

  **components/common/Modal.vue** 생성

- `slot=" "` : 특정 컴포넌트의 일부 UI를 재사용 할 수 있는 기능
- `v-on:click=" "` == `@click=" "` 같은 의미로 다음과 같이 축약하여 작성 가능

## 트렌지션

- 기본적으로`v-enter-to` 와 `v-leave`를, `v-leave-to` 와 `v-enter`를 같이 사용
  - `v-enter` : 처음 이펙트가 시작 됐을 때 상태
  - `v-enter-to` : 이펙트가 시작되고 끝났을 때 상태
  - `v-enter-active` : `v-enter` + `v-enter-to`
  - `v-leave` : 기존 상태
  - `v-leave-to` : 이펙트가 없어진 상태
  - `v-leave-active` : `v-leave` + `v-leave-to`

## Vuex

- 무수히 많은 컴포넌트의 데이터를 관리하기 위한 상태 관리 패턴이자 라이브러리
- React의 Flux 패턴에서 기인함
- Vuex 컨셉
  - **State** : 컴포넌트 간에 공유하는 데이터 `data( )`
  - **View** : 데이터를 표시하는 화면 `template`
  - **Action** : 사용자의 입력에 따라 데이터를 변경하는 `methods`
- Vuex 구조
  - **컴포넌트 > 비동기 로직 > 동기 로직 > 상태**

## Flux

- MVC 패턴의 복잡한 데이터 흐름 문제를 해결하는 개발 패턴 - Unidirectional data flow
- **Action > Dispatcher > Model > View**
  1. **action** : 화면에서 발생하는 이벤트 또는 사용자의 입력
  2. **dispatcher** : 데이터를 변경하는 방법, 메서드
  3. **model** : 화면에 표시할 데이터
  4. **View** : 사용자에게 비춰지는 화면
- 알아두면 상식 : MVC 패턴 - **Controller > Model <=> View**

## Vuex 사용

```bash
npm i vuex --save
```

- src/store/store.js

```javascript
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  //
});
```

- src/main.js ( 변수는 `{ }` 사용 )

```javascript
import { createApp } from "vue";
import App from "./App.vue";

// vuex
import { store } from "./store/store";

const app = createApp(App);
app.use(store);

// createApp(App).mount('#app');
app.mount(`#app`);
```

## Vuex 기술 요소

- **state** : 여러 컴포넌트에서 공유되는 `data`
- **getters** : 연산된 state 값을 접근하는 속성 `computed`
- **mutations** : state 값을 변경하는 이벤트 로직 또는 메서드 `methods`
- **actions** : 비동기 처리 로직을 선언하는 메서드 `aysnc methods`

### state

- 여러 컴포넌트 간에 공유할 데이터 - **상태**

```javascript
// Vue
data: {
  message: "Hello";
}

<p>{{ message }}</p>;

// Vuex
state: {
  message: "Hello";
}
```

```html
<p>{{ this.$store.state.message }}</p>
```

### getters

- state 값을 접근하는 속성이자 `computed( )` 처럼 미리 연산된 값을 접근하는 속성

```javascript
// store.js
state: {
  num: 10
},
getters: {
  getNumber(state) {
    return state.num;
  },
  doubleNumber(state) {
    return state.num * 2;
  }
}
```

```html
<p>{{ this.$store.getters.getNumber }}</p>
<p>{{ this.$store.getters.doubleNumber }}</p>
```

### mutations

- state의 값을 변경할 수 있는 **유일한 방법**이자 메서드
- mutaion은 `commit( )` 으로 동작시킴

```javascript
// store.js
state: { num: 10 },
mutations: {
  printNumbers(state) {
    return state.num
  },
  sumNumbers(state, anotherNum) {
    return state.num + anotherNum;
  }
}

// App.vue
this.$store.commit('printNumbers');
this.$store.commit('sumNumbers', 20);
```

- state를 변경하기 위해 mutaions를 동작시킬 때 인자(payload)를 전달 가능

```javascript
// store.js
state: { storeNum: 10 },
mutations: {
  modifyState(state, payload) {
    console.log(payload.str);
    return state.storeNum += payload.num;
  }
}

// App.vue
this.$store.commit('modifyState', {
  str: 'passed from payload',
  num: 20
});
```

### state는 왜 직접 변경하지 않고 mutations로 변경할까?

- 여러 개의 컴포넌트에서 state 값을 변경하는 경우 **어느 컴포넌트에서 해당 state를 변경했는지 추적하기가 어려움**
- 특정 시점에 어떤 컴포넌트가 state를 접근하여 변경한 건지 확인하기 어려움
- 따라서, 뷰의 반응성을 거스르지 않게 명시적으로 상태 변화를 수행. **반응성, 디버깅, 테스팅 혜택**

### actions

- 비동기 처리 로직을 선언하는 메서드. 비동기 로직을 담당하는 mutations
- 데이터 요청, Promise, ES6 async와 같은 비동기 처리는 모두 actions에 선언

```javascript
// store.js
mutations: {
  setData(state, fetchedData) {
    state.product = fetchedData;
  }
},
actions {
  fetchProductData(context) { // context로 store의 메서드와 속성 접근
    return axios.get('https://domain.com/products/1')
                .then(response => context.commit('setData', response));
  }
}

// App.vue
methods: {
  getProduct() {
    this.$store.dispatch('fetchProductData');
  }
}
```

### 왜 비동기 처리 로직은 actions에 선언해야 할까?

- 언제 어느 컴포넌트에서 해당 state를 호출하고, 변경했는지 확인하기가 어려움
- 여러 개의 컴포넌트에서 mutations로 시간 차를 두고 state를 변경하는 경우
  - state 값의 변화를 추적하기 어렵기 때문에 mutations 속성에는 동기 처리 로직만 넣어야 함

## Helper

- store에 있는 4가지 속성들을 간편하게 사용하는 방법
  - state → mapState
  - getters → mapGetters
  - mutations → mapMutations
  - actions → mapActions

## Helper 사용법

- helper를 사용하고자 하는 vue 파일에서 해당 helper를 로딩
- ...는 ES6의 Object Spread Operator

```javascript
// App.vue
import { mapState } from 'vuex'
import { mapGetters } from 'vuex'
import { mapMutations } from 'vuex'
import { mapActions } from 'vuex'

export default {
  computed() { ...mapState(['num']), ...mapGetters(['countedNum']) },
  methods: { ...mapMutations(['clickBtn']), ...mapActions(['asyncClickBtn']) }
}
```

### mapState

- Vuex에 선언한 state 속성을 뷰 컴포넌트에 더 쉽게 연결해주는 helper

```javascript
// App.vue
import { mapState } from 'vuex'

computed() {
  ...mapState(['num'])
  // num() { return this.$store.state.num; }
}

// store.js
state: {
num: 10
}
```

```html
<!-- <p>{{ this.$store.state.num }}</p> -->
<p>{{ this.num }}</p>
```

### mapGetters

- Vuex에 선언한 getters 속성을 뷰 컴포넌트에 더 쉽게 연결해주는 helper

```javascript
// App.vue
import { mapGetters } from 'vuex'

computed() { ...mapGetters(['reverseMessage']) }

// store.js
getters: {
  reverseMessage(state) {
    return state.msg.split('').reverse().join('');
  }
}
```

```html
<!-- <p>{{ this.$store.getters.reverseMessage }}</p> -->
<p>{{ this.reverseMessage }}</p>
```

### mapMutations

- Vuex에 선언한 mutations 속성을 뷰 컴포넌트에 더 쉽게 연결해주는 helper

```javascript
// App.vue
import { mapMutations } from 'vuex'

methods: {
    ...mapMutations(['clickBtn']),
  authLogin() {},
  displayTable() {}
}

// store.js
mutations: {
  clickBtn(state) {
    alert(state.msg);
  }
}
```

```html
<button @click="clickBtn">popup message</button>
```

### mapActions

- Vuex에 선언한 actions 속성을 뷰 컴포넌트에 더 쉽게 연결해주는 helper

```javascript
// App.vue
import { mapActions } from 'vuex'

methods: {
  ...mapactions(['delayClickBtn']),
}

// store.js
actions: {
  delayClickBtn(context) {
    setTimeout(() => context.commit('clickBtn'), 2000);
  }
}
```

```html
<button @click="delayClickBtn">delay popup message</button>
```

### helper를 유연하게 사용

- Vuex에 선언한 속성을 그대로 컴포넌트에 연결

```javascript
// 배열 리터럴
...mapMutations([
  'clickBtn', // 'clickBtn': clickBtn
  'addNumber' // addNumber(인자)
])
```

- Vuex에 선언한 속성을 컴포넌트의 특정 메서드에 연결

```javascript
// 객체 리터럴
...mapMutations({
  popupMsg: 'clickBtn' // 컴포넌트 메서드 명: store의 뮤테이션 명
})
```
