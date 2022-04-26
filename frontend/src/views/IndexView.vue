<template>
  <div style="text-align: center">{{ name }}</div>
  <router-link to="/login"
    ><div style="text-align: center">login</div></router-link
  >
</template>

<script>
import axios from "axios";

export default {
  name: "indexView",
  data() {
    return {
      name: "Hello",
    };
  },
};
</script>

<style scoped></style>
