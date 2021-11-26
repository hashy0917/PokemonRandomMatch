<template>
  <div class="hello">
    <h1>現在の待機人数{{ msg }}人</h1>
  </div>
</template>

<script>
export default {
  name: 'PokemonRandomMatch',
  props: {
    msg: Intl
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