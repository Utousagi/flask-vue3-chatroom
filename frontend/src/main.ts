import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueSocketIO from "vue-3-socket.io";
import SocketIO from "socket.io-client";
import axios from "axios";
import store from "@/store";

axios.interceptors.request.use((config) => {
  const token = store.state.token;
  if (token) {
    config.headers!.Authorization = "Bearer " + token;
  }
  return config;
});

createApp(App)
  .use(router)
  .use(store)
  .use(
    new VueSocketIO({
      debug: true,
      connection: SocketIO(":8082"),
      vuex: {
        store,
        actionPrefix: "SOCKET_",
        mutationPrefix: "SOCKET_",
      },
    })
  )
  .mount("#app");
