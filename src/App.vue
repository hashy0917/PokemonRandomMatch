<template>
  <div id="app">
    <img class="monsterball" alt="monster ball logo" src="./assets/main_pb.png">
    <HelloWorld msg="Welcome to PokemonRandomMatch Server"/>
    <Top></Top>
    <Wait count="" v-show="false"></Wait>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Top from './components/Top'
import Wait from './components/Wait'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Top,
    Wait,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
@media (prefers-reduced-motion: no-preference) {
   .monsterball{
    animation: App-logo-spin infinite 6000ms linear;
  }
}
@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
