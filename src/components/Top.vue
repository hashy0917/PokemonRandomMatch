<template>
  <div class="hello">
    <form @click.prevent method="post">
      <input v-model="myname" placeholder="トレーナー名を入力してください" />
      <p>トレーナー名は {{ myname }} でよろしいですか？</p>
      <button type="submit" v-on:click="openModal">はい</button>
      <button type="submit" v-on:click="clear">いいえ</button>
    </form>

    <MatchingWait :apidata1=code :apidata2=name v-show="showContent" v-on:from-child="closeModal"></MatchingWait>

  </div>
</template>

<script>
import MatchingWait from "@/components/MatchingWait";

export default {
  name: 'PokemonRandomMatch',
  props: {
    myname: String,
    code: String,
    name: String,
    showContent: Boolean,
    apidata1: String,
    apidata2: String,
  },
  components: {
    MatchingWait
  },
  methods:{
    clear: function (){
      this.myname = "";
    },
    push: function (){
      this.axios.post("/api/v1", this.myname)
          .then(response => {
            this.code = response.data.code
            this.name = response.data.name
          })
    },
    openModal: function (){
      if(!this.myname){
        alert('トレーナー名を入力してください')
        return
      }
      this.push()
      this.showContent = true
    },
    closeModal: function(){
      this.showContent = false
    },
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