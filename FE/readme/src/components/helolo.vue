<template>
    <div id="app">
      <div :style="computedStyledObject">
        Hello
      </div>
      <button @click="update()">Click</button>
    </div>
</template>
<script>
      new Vue({
        el: '#app',
        data: {
          classObject: {
            red: 'red',
            size: '30px'
          }
        },
        computed: {
          computedStyledObject() {
            return {
              color: this.classObject.red,
              size: this.classObject.size
            };
          }
        },
        methods: {
          update() {
            (this.classObject.red = 'blue'), (this.classObject.size = '50px');
          }
        }
      });
    </script>