<template>
  <main class="main">
    <div class="b-container">
      <div class="b-title"><b>登 录</b></div>
      <div class="b-form">
        <a-form>
          <div class="b-input">
            <label>
              <a-input
                placeholder="用户名"
                v-model="username"
                :error="inputError"
              >
                <template #prefix>
                  <icon-user />
                </template>
              </a-input>
            </label>
          </div>
          <div class="b-input">
            <label>
              <a-input-password
                placeholder="密码"
                v-model="password"
                :error="inputError"
              >
                <template #prefix>
                  <icon-unlock />
                </template>
              </a-input-password>
            </label>
          </div>
          <div class="b-to-register">
            没有账号?
            <router-link to="/register">点此注册</router-link>
          </div>
          <div class="b-submit">
            <a-button type="primary" long @click="login">登录</a-button>
          </div>
        </a-form>
        <div class="b-error" v-show="error">{{ error }}</div>
      </div>
    </div>
  </main>
</template>

<script>
import { IconUser, IconUnlock } from "@arco-design/web-vue/es/icon";
import axios from "axios";

export default {
  name: "LoginView",
  components: {
    IconUser,
    IconUnlock,
  },
  data() {
    return {
      username: "",
      password: "",
      passwordHash: "",
      error: "",
      inputError: false,
    };
  },
  methods: {
    async login() {
      try {
        const res = await axios.post("/api/auth/login", {
          username: this.username,
          password: this.password,
        });
        const resData = res.data;
        if (resData.code === 200) {
          this.error = "";
          this.$store.commit("setToken", res.headers["access_token"]);
          this.$store.commit("setUser", resData.data);
          this.$socket.emit("user_login", this.username);
          setTimeout(() => {
            this.$router.replace("/chatroom");
          }, 1000);
        } else if (resData.code === 400) {
          this.mkErrorHint();
          this.error = resData.message;
        }
      } catch (e) {
        console.log(e);
      }
    },
    mkErrorHint() {
      this.inputError = true;
      setTimeout(() => {
        this.inputError = false;
      }, 200);
    },
    onKeyDown(e) {
      if (e.keyCode === 13) {
        this.login();
      }
    },
  },
  mounted() {
    window.addEventListener("keydown", this.onKeyDown);
  },
};
</script>

<style lang="scss">
$bm: 70px;
$ibm: 14px;

.main {
  height: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  opacity: 0.95;

  .b-container {
    margin: 10px;
    height: 350px;
    width: 400px;
    border-radius: 5px;
    background-color: #cce6f388;

    .b-title {
      margin: $bm $bm 10px $bm;
      font-size: 17px;
      text-align: center;
    }

    .b-form {
      margin: 5px $bm $bm $bm;

      .b-input {
        margin: $ibm $ibm 0 $ibm;
      }

      .b-to-register {
        text-align: left;
        font-size: 10px;
        margin: 15px $ibm 3px $ibm;

        a {
          font-size: 10px;
        }
      }

      .b-submit {
        margin: 0 $ibm 0 $ibm;
        opacity: 0.9;
      }

      .b-error {
        display: block;
        height: 14px;
        margin: 5px $ibm 0 $ibm;
        font-size: 13px;
        color: #e04b4b;
        text-align: left;
      }
    }
  }
}
</style>
