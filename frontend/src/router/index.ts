import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import store from "@/store";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "index",
    component: () => import("@/views/IndexView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/authViews/LoginView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/authViews/RegisterView.vue"),
  },
  {
    path: "/chatroom",
    name: "chatroomList",
    component: () => import("@/views/chatroomViews/RoomListView.vue"),
  },
  {
    path: "/chatroom/:roomId",
    name: "chatroom",
    component: () => import("@/views/chatroomViews/ChatroomView.vue"),
  },
  {
    path: "/404",
    name: "pageNotExist",
    component: () => import("@/views/ExceptionView/NotFoundView.vue"),
  },
  {
    path: "/:catchAll(.*)",
    redirect: "/404",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from) => {
  console.log("route: " + from.path + " " + to.path);
  if (to.path == "/login" || to.path == "/register") {
    return true;
  } else if (store.state.token) {
    return true;
  }
  // if(from.path == "/" && /^\d+$/.test(to.path) {
  //
  // }
  return "/login";
});

export default router;
