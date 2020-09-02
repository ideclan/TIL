## Courses

### Vue.js Bootcamp

- [Vue.js 시작하기 - Age of Vue.js](https://www.inflearn.com/course/Age-of-Vuejs)
  , 인프런
- [Vue.js 중급 강좌 - 웹앱 제작으로 배워보는 Vue.js, ES6, Vuex](https://www.inflearn.com/course/vue-pwa-vue-js-%EC%A4%91%EA%B8%89), 인프런
- [트렐로 개발로 배우는 Vuejs, Vuex, Vue-Router 프론트엔드 실전 기술](https://www.inflearn.com/course/vuejs), 인프런

### Vue CLI로 프로젝트 생성

```bash
$ vue create vue-todo

# default (babel, eslint) 기본값
# Manually select features 여러가지 기능을 선택하여 구성이 가능

$ cd vue-todo
$ npm run serve
```

### 컴포넌트 생성 및 등록

- my-project/src/components 경로에 TodoHeader.vue 생성

```jsx
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

```jsx
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

### Favicon, Icon, Font, 반응형 태그 설정

**index.html에 적용**

- Favicon : [https://www.favicon-generator.org/](https://www.favicon-generator.org/)

```html
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
<link rel="icon" href="/favicon.ico" type="image/x-icon">
```

- Fontawesome Icon

```html
<link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>
```

- Google Font Ubuntu

```html
<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Ubuntu" />
```

- 반응형 태그 설정 (모바일)

```html
<meta name="viewport" content="width=device-width,initial-scale=1.0">
```

### Header 컴포넌트 구현

**TodoHeader.vue**

- **scoped** : 해당 컴포넌트 안에서만 적용하는 설정
- 알아두면 상식
    - font-weight은 글자 굵기
    - margin에서 px단위가 아닌 rem을 사용하면 글자 굵기에 비율이 정해짐

```jsx
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

**App.vue**

```jsx
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

**TodoInput.vue**

- **v-model** : Input에 입력된 텍스트 값을 동적으로 Vue 인스턴스와 연결하는 역할
- **v-on:click** : 클릭했을 때 호출되는 method 정의
- **v-on:keyup.enter** : enter를 눌렀을 때 호출되는 method 정의
- Fontawesome Icon을 사용하여 <span><i>로 버튼처럼 만들 수 있음
- 외부 App.vue에서 정의한 style을 사용할 수 있음
- 아직 DB를 사용하지 않으므로 localStorage API를 사용하여 저장된 key, value는 크롬 웹 브라우저 > 개발자 도구 > Application > Storage > Local Storage > localhost:8080에서 확인 가능

```jsx
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

**TodoList.vue**

- **created** : 인스턴스가 생성되면서 호출되는 라이프 사이클 훅(생성되는 시점에 호출)
- **this** : 같은 인스턴스를 가르키기 때문에 this로 data의 todoItems 값에 접근이 가능
- **v-for** : todoItems 배열 안에서 todoItem 개수만큼 반복 (v-for를 사용할 때는 v-bind:key 사용, index는 꼭 사용하지 않아도 됨)
- 알아두면 상식 : JS API **splice( )** 해당 배열에서 값을 지우고 새로운 배열을 반환 ≠ **slice( )**

    **TodoInput.vue** 에서 **JSON.stringify( )** 로 현재는 데이터가 String 타입이므로 객체로 변환하려면 **JSON.parse( )** 사용

- **v-bind:class="{클래스명: 조건}"** : 조건이 false면 해당 클래스가 적용되지 않음

```jsx
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

**TodoInput.vue > addTodo 수정**

- 알아두면 상식 : **JSON.stringify( )** JS 객체를 String으로 변환

```jsx
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

**TodoFooter.vue**

```jsx
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

### 현재 앱 구조의 문제점

- 로컬 스토리지에 저장 또는 삭제는 되지만 리스트가 바로 갱신이 되지 않음 (새로고침을 해야 갱신이 됨)
- 하나의 컴포넌트에서 이벤트가 발생하여 데이터 변경이 일어났을 때 **다른 컴포넌트에서는 인식을 하지 못함**

### 리팩토링

- 다음과 같은 구조인 방식인 **컨테이너 컴포넌트** 설계 기법으로 변경
    - App.vue(상위 컴포넌트)에서는 데이터를 조작하고 Propsdata를 내려줌
    - 나머지(하위 컴포넌트)에서는 UI 표현만 하고 이벤트를 올려줌

- **v-bind: 내려보낼 props 속성 이름="현재 위치의 컴포넌트 데이터"**
- **v-on: 하위 컴포넌트에서 발생시킨 이벤트 이름="현재 컴포넌트의 메서드 명"**
    - **this.$emit('이벤트 이름', 인자1, 인자2 ...)** 하위 컴포넌트에서 해당 이벤트 이름으로 이벤트를 발생시켜 상위 컴포넌트에 전송

**App.vue**

```jsx
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

**TodoList.vue**

```jsx
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

**TodoInput.vue**

```jsx
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

**TodoFooter.vue**

```jsx
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