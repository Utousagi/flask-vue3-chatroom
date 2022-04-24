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
      name: "uto",
    };
  },
  async mounted() {
    this.name = (await axios.get("http://localhost:5000/")).data;
  },
};
</script>

<style scoped></style>
