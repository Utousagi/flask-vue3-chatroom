<template>
  <main>
    <h2>Oops，404</h2>
    <h4>3秒后将返回首页</h4>
  </main>
</template>

<script>
export default {
  name: "NotFoundView",
  mounted() {
    setTimeout(() => {
      this.$router.replace("/chatroom");
    }, 3000);
  },
};
</script>

<style lang="scss">
main {
  height: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>
