<template>
  <div class="msg-b-container">
    <div class="msg-b-avatar">
      <a-avatar :size="32" style="background-color: #3370ff">
        <img alt="avatar" :src="avatar" v-if="avatar" />
        <icon-user v-else />
      </a-avatar>
    </div>
    <div class="msg-b-right">
      <div class="msg-b-name">{{ name }}</div>
      <div class="msg-b-content">
        {{ content }}
      </div>
    </div>
  </div>
</template>

<script>
import { IconUser } from "@arco-design/web-vue/es/icon";

export default {
  name: "chatMessage",
  components: {
    IconUser,
  },
  props: {
    name: "",
    content: "",
    avatar: "",
  },
};
</script>

<style lang="scss">
.msg-b-container {
  display: flex;
  flex-direction: row;
  padding: 10px;

  .msg-b-avatar {
    display: block;
    width: 32px;
    height: 32px;
    opacity: 0.95;
  }

  .msg-b-right {
    width: 500px;
    margin: 0 0 0 10px;

    .msg-b-name {
      color: #b9b9b9;
    }

    .msg-b-content {
      overflow-x: hidden;
      overflow-y: hidden;
    }
  }
}
</style>
