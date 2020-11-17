<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <CardBuilder/>
  </div>
</template>

<script>
import CardBuilder from './components/CardBuilder.vue'

export default {
  name: 'App',
  components: {
    CardBuilder
  }
}
</script>

<style lang="scss">
@import './assets/styles/main.scss';

</style>
