import { createStore } from "vuex";

const store = createStore({
  state: {
    token: "",
    user: {
      username: "",
      avatar: "",
    },
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem("access_token", token);
    },
    delToken(state) {
      state.token = "";
      localStorage.removeItem("access_token");
    },
    setUser(state, user) {
      state.user = user;
      localStorage.setItem("user_info", JSON.stringify(user));
    },
  },
});
if (localStorage.getItem("access_token")) {
  store.commit("setToken", localStorage.getItem("access_token"));
}
if (localStorage.getItem("user_info")) {
  store.commit("setUser", JSON.parse(localStorage.getItem("user_info")!));
}

export default store;
