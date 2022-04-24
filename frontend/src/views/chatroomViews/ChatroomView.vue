<template>
  <main class="main">
    <div class="b-container">
      <div class="b-header">
        <div class="b-id">
          <b>ID: {{ roomId }}</b>
        </div>
        <div class="b-title">
          <b>{{ roomName }}</b>
        </div>
        <div class="b-button">
          <a-button @click="leave">退 出</a-button>
        </div>
      </div>
      <div class="b-main">
        <div class="b-chat">
          <div class="b-message">
            <a-list :bordered="false">
              <chat-message
                v-for="log in this.logs"
                :name="log.username"
                :content="log.content"
                :avatar="log.avatar"
              ></chat-message>
            </a-list>
          </div>
          <div class="b-input">
            <a-textarea
              :auto-size="{ minRows: 4, maxRows: 4 }"
              style="background-color: transparent; border: none"
              v-model="message"
            />
            <div class="b-button">
              <a-button type="primary" @click="send">发送</a-button>
            </div>
          </div>
        </div>
        <div class="b-member"></div>
      </div>
    </div>
  </main>
</template>

<script>
import chatMessage from "@/components/chatMessage.vue";
import axios from "axios";

export default {
  name: "chatroomView",
  components: {
    chatMessage,
  },
  data() {
    return {
      roomId: this.$route.params.roomId,
      roomName: "",
      logs: [],
      message: "",
      nowTime: 0,
      hasPre: true,
    };
  },
  methods: {
    send() {
      console.log("check");
      if (this.message !== "") {
        this.$socket.emit(
          "send_message",
          this.message,
          this.$store.state.user.username,
          this.$store.state.user.avatar,
          this.roomId
        );
        setTimeout(() => {
          document
            .getElementsByClassName("msg-b-container")
            .item(document.getElementsByClassName("msg-b-container").length - 1)
            .scrollIntoView(false);
        }, 20);
        this.message = "";
      }
    },
    leave() {
      this.$router.push("/chatroom");
    },
    onKeyDown(e) {},
    beforeUnloadHandler(e) {
      this.$socket.emit(
        "leave_room",
        this.$store.state.user.username,
        this.roomId
      );
    },
  },
  async beforeCreate() {
    const res = await axios.get(
      "http://localhost:5000/api/chat/checkRoomExist",
      {
        params: {
          roomId: this.$route.params.roomId,
        },
      }
    );
    const resData = res.data;
    if (!resData.data) {
      await this.$router.replace("/404");
    }
    this.roomName = resData.data["name"];
  },
  async mounted() {
    window.addEventListener("keydown", this.onKeyDown);
    window.addEventListener("unload", this.beforeUnloadHandler);
    this.$socket.emit(
      "join_room",
      this.$store.state.user.username,
      this.roomId
    );
    const res = await axios.get("http://localhost:5000/api/chat/getMessage", {
      params: {
        roomId: this.roomId,
        time: Date.now(),
      },
    });
    const resData = res.data;
    if (resData.code === 200) {
      this.logs = resData.data;
      this.nowTime = this.logs[0]["time"];
    }
    await this.$nextTick(() => {
      document
        .getElementsByClassName("msg-b-container")
        .item(document.getElementsByClassName("msg-b-container").length - 1)
        .scrollIntoView(false);
    });
  },
  unmounted() {
    window.removeEventListener("keydown", this.onKeyDown);
    window.removeEventListener("unload", this.beforeUnloadHandler);
  },
  sockets: {
    broadcast_message(message) {
      this.logs.push(message);
      console.log("logs: " + this.logs.join());
    },
  },
};
</script>

<style lang="scss">
.main {
  height: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  .b-container {
    width: 800px;
    height: 600px;
    border-radius: 6px;
    background-color: #cce6f388;

    .b-header {
      width: inherit;
      display: flex;
      align-items: center;
      height: 60px;
      border-radius: 6px 6px 0 0;
      background-color: #efefef77;

      .b-id {
        margin: 20px;
      }

      .b-title {
        font-size: 17px;
        margin: 0 auto;
      }

      .b-button {
        margin: 30px;
      }
    }

    .b-main {
      display: flex;
      height: 510px;
      flex-direction: row;

      .b-chat {
        height: inherit;
        width: 580px;
        //background-color: #cce6f3;

        .b-message {
          height: 350px;
          width: inherit;
          margin: 15px;
          border-radius: 6px;
          background-color: #f3edcc7f;
          overflow-y: scroll;
        }

        .b-input {
          padding: 5px 0 10px 0;
          margin: 15px 15px 0 15px;
          width: inherit;
          border-radius: 6px;
          background-color: #cce6f37f;

          .b-button {
            text-align: right;
            margin: 0 20px;
            opacity: 0.9;
          }
        }
      }

      .b-member {
        height: inherit;
        width: 170px;
        border-radius: 6px;
        margin: 15px 20px 15px 30px;
        background-color: #bff1d899;
      }
    }
  }
}
</style>
