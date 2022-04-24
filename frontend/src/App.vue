<template>
  <router-view />
</template>

<script setup lang="ts"></script>

<style lang="scss">
html {
  height: 100%;
  width: 100%;

  body {
    height: inherit;
    margin: 0;
    position: fixed;
    top: 0;
    left: 0;
    min-width: 100%;
    z-index: -10;
    zoom: 1;
    background: url("assets/bg.png") no-repeat center 0;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;

    a {
      color: dodgerblue;
      text-decoration: None;

      &:hover {
        color: #a988f5;
      }

      &:active {
        color: #5f2dd3;
      }
    }
    ::-webkit-scrollbar {
      width: 8px;
      background-color: transparent;
    }
    ::-webkit-scrollbar-thumb {
      border-radius: 5px;
      background-color: #a0a0a033;

      &:hover {
        background-color: #a0a0a088;
      }
    }

    #app {
      height: inherit;
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      color: #2c3e50;
    }
  }
}
</style>
