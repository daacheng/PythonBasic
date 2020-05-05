# Vue基础学习.md
## 一、Vue对象

        var app5 = new Vue({
                    'el': '#app-5',
                    'data': {
                        message: '你好啊',
                        href: 'www.baidu.com',
                        webtag: '<a href="www.baidu.com">百度</a>'
                    },
                    methods: {
                        reversemessage: function(){
                            this.message = this.message.split('').reverse().join('')
                        }
                    }
                })

## 二、属性绑定
* v-bind: 绑定Vue对象中的数据到HTML标签的属性中。
* v-html: 如果Vue对象中的数据是段HTML代码，可以用v-html，直接输出。

        <a v-bind:href="href">链接</a>
        <p v-html="webtag"></p>

## 三、事件v-on（单击、双击、鼠标移动）

        <button v-on:click="methods">点击执行method方法</button>
        <button v-on:dblclick="methods">双击执行method方法</button>
        <button v-on:mousemove="methods">鼠标移动时执行method方法</button>

## 四、事件修饰符

        <!-- 事件只执行一次 -->
        <a v-on:click.once="doThis"></a>

        <!-- 阻止单击事件继续传播 -->
        <a v-on:click.stop="doThis"></a>

        <!-- 提交事件不再重载页面 -->
        <form v-on:submit.prevent="onSubmit"></form>

        <!-- 修饰符可以串联 -->
        <a v-on:click.stop.prevent="doThat"></a>

        <!-- 只有修饰符 -->
        <form v-on:submit.prevent></form>
## 五、键盘事件
全部的按键别名：

.enter
.tab
.delete (捕获“删除”和“退格”键)
.esc
.space
.up
.down
.left
.right

        <!-- 输入回车的时候执行 -->
        <input v-on:keyup.enter="submit">
        
## 六、双向数据绑定（v-model）
* Vue对象获取html标签中的数据，通过ref,可以通过 this.$refs.name.value获取前台input中输入的内容。

        <input ref="name" type="text" v-on:keyup="method">
        
* 第二种方法，通过v-model，指定html与vue对象中的name属性进行绑定。(在html中输入的时候，就相当于把输入的值赋给vue的name)

        <input ref="name" type="text" v-model="name">
        
## 七、计算属性(computed)
**methods中的方法一旦触发，所有方法都会执行一遍。计算属性会对他们基于的依赖进行缓存，只有当他们依赖的值发生变化时，才会重新进行计算。**
## 八、绑定css样式
        
        <div v-bind:class={class:true}></div>

## 九、指令v-if
## 十、指令v-for
## 十一、搭建脚手架cli
* 安装node.js和npm
* 全局安装vue-cli : npm install --global vue-cli
* 创建一个基于webpack的新项目： vue init webpack myproject
* cd myproject
* 安装依赖 : npm install
* 运行 npm run dev

## 十二、组件结构app.vue

        <template>
          <div id="app">
            {{ title }}
            <users></users>
          </div>
        </template>

        <script>
        import users from './components/users'
        export default {
          name: 'App',
          data () {
            return {
              title: "第一个Vue脚手架！"
            }
          },
          //注册组件
           components:{
              'users':users
           }
        }
        </script>

        <style>

        </style>

## 十三、子组件往父组件传值
**有时候，子组件中需要点击某个按钮，控制父组件中部分组件的显示与隐藏**
* 1. 子组件点击的时候，执行方法，方法中使用$emit来触发一个自定义事件，并传递一个参数。

                showMain(){
                        //子组件往父组件传值，控制首页轮播显示
                        this.$emit("listenChildEvent", "true");
                      }
        
* 2. 在父组件中的子标签中监听该自定义事件并添加一个响应该事件的处理方法。

                <Header v-on:listenChildEvent="showMain">

                showMain:function(isShowMain){
                      if (isShowMain == "true"){
                        this.isshow = true;
                      }else{
                        this.isshow = false;
                      }
                    }

## 十四、控制组件动态加载
v-bind:is="currentComponent"  :  currentComponent指定你要加载的组件名称

                <component v-bind:is="currentComponent"></component>
