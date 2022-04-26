<template>
  <a-modal
    v-model:visible="modalVisible"
    modal-class="modal"
    :footer="false"
    :closable="false"
    :mask-closable="true"
    @close="onClose"
    width="440px"
  >
    <div class="m-container">
      <div class="b-header"><b>创 建 房 间</b></div>
      <a-divider />
      <div class="b-form">
        <a-form model="">
          <div class="b-input">
            <label>
              名称
              <a-input placeholder="" v-model="name"> </a-input>
            </label>
          </div>
          <div class="b-textarea">
            简介
            <a-textarea
              :auto-size="{ minRows: 5, maxRows: 5 }"
              :max-length="100"
              :show-word-limit="true"
              v-model="description"
            />
          </div>
          <div>
            <label>
              私有
              <a-switch size="small" v-model="private" />
            </label>
          </div>
          <div class="b-input">
            <label>
              密码
              <a-input-password :disabled="!private" v-model="secret">
              </a-input-password>
            </label>
          </div>
          <div class="b-submit">
            <div class="b-button">
              <a-button type="primary" @click="create">创 建</a-button>
            </div>
            <div class="b-button">
              <a-button @click="cancel">取 消</a-button>
            </div>
          </div>
        </a-form>
      </div>
    </div>
  </a-modal>
</template>

<script>
import axios from "axios";

export default {
  name: "createRoomModal",
  data() {
    return {
      modalVisible: false,
      name: "",
      description: "",
      private: false,
      secret: "",
    };
  },
  methods: {
    async create() {
      if (!this.private) {
        this.secret = "";
      }
      if (!this.name) {
        return;
      }
      const res = await axios.post("/api/chat/createRoom", {
        name: this.name,
        description: this.description,
        private: this.private,
        secret: this.secret,
      });
      const resData = res.data;
      if (resData.code === 200) {
        const roomId = resData.data["id"];
        setTimeout(() => {
          this.modalVisible = false;
          this.$router.push("/chatroom/" + roomId);
        }, 1000);
      }
    },
    cancel() {
      this.modalVisible = false;
    },
    show() {
      this.modalVisible = true;
    },
    onClose() {
      this.name = "";
      this.description = "";
      this.private = false;
      this.secret = "";
    },
  },
};
</script>

<style lang="scss">
.m-container {
  opacity: 0.9;

  .b-header {
    font-size: 17px;
    text-align: center;
  }

  .b-form {
    margin: 20px;

    .b-input {
    }

    .b-submit {
      display: flex;
      justify-content: center;
      margin: 10px;

      .b-button {
        margin: 10px;
      }
    }
  }
}

.modal {
  background-color: #7d9cea92;
}
</style>
