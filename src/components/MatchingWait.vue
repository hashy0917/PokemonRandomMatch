<template>
  <div id="overlay" v-show="showContent">
    <div id="content" >
      <p>{{ apidata2 }}</p>
      <p>{{ apidata1 }}</p>
      <p><button v-on:click="clickEvent">マッチングしました</button></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MatchingWait",
  props: {
    apidata1: String,
    apidata2: String,
  },
  methods :{
    clickEvent: function(){
      this.$emit('from-child')
    },
  }
}
</script>

<style scoped>
#content{
  z-index:2;
  width:50%;
  padding: 1em;
  background:#fff;
}
#overlay{
  z-index:1;

  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color:rgba(0,0,0,0.5);

  display: flex;
  align-items: center;
  justify-content: center;
}
</style>