<template>
  <div class="hello">
    <form @click.prevent>
      <input v-model="msg" placeholder="トレーナー名を入力してください" />
      <p>トレーナー名は {{ msg }} でよろしいですか？</p>
      <button type="submit" v-on:click="push">はい</button>
      <button type="submit" v-on:click="clear">いいえ</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'PokemonRandomMatch',
  props: {
    msg: String
  },
  methods:{
    clear: function (){
      this.msg = ""
    },
    push: function (){

    }
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>