<template>
  <main class="main">
    <create-room-modal ref="modal" />
    <div class="b-container">
      <div class="b-search">
        <div class="b-input">
          <a-input
            size="small"
            placeholder="支持通过ID精确查询或名称模糊查询"
            allow-clear
            v-model="keyword"
          />
        </div>
        <div class="b-button">
          <a-button id="search-button" size="small" @click="search"
            >搜 索</a-button
          >
        </div>
        <div class="b-button">
          <a-button id="reset-button" size="small" @click="reset"
            >重 置</a-button
          >
        </div>
        <div class="b-button b-create-button">
          <a-button id="create-button" size="small" @click="showModal"
            >创建房间</a-button
          >
        </div>
      </div>
      <div class="b-room-list">
        <a-table
          :columns="columns"
          :data="roomData"
          :bordered="false"
          page-position="bottom"
          @row-click="joinRoom"
        />
      </div>
    </div>
  </main>
</template>

<script>
import axios from "axios";
import CreateRoomModal from "@/components/createRoomModal.vue";

export default {
  name: "RoomListView",
  components: { CreateRoomModal },
  data() {
    const columns = [
      {
        title: "ID",
        dataIndex: "id",
        width: 110,
      },
      {
        title: "名称",
        dataIndex: "name",
        width: 130,
        ellipsis: true,
      },
      {
        title: "简介",
        dataIndex: "description",
        width: 220,
        ellipsis: true,
      },
      {
        title: "创建时间",
        dataIndex: "createTime",
        width: 200,
      },
      {
        title: "私密",
        dataIndex: "private",
      },
    ];

    return {
      columns,
      roomData: [],
      keyword: "",
    };
  },
  methods: {
    joinRoom(tableData) {
      this.$router.push("/chatroom/" + tableData.id);
    },
    async search() {
      const res = await axios.get("http://localhost:5000/api/chat/searchRoom", {
        params: {
          keyword: this.keyword,
        },
      });
      const resData = res.data;
      this.roomData = resData.data;
    },
    async reset() {
      const res = await axios.get("http://localhost:5000/api/chat/listRoom");
      const resData = res.data;
      this.roomData = resData.data;
    },
    showModal() {
      this.$refs.modal.show();
    },
  },
  async mounted() {
    await this.reset();
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
  opacity: 0.95;

  .b-container {
    margin: 10px;
    height: 600px;
    width: 800px;
    border-radius: 5px;
    background-color: #cce6f388;

    .b-search {
      margin: 10px;
      display: flex;

      .b-input {
        width: 270px;
        margin: 0 20px 0 20px;
      }

      .b-button {
        margin: 0 10px;
      }

      .b-create-button {
        margin-left: 170px;
      }

      #search-button {
        background-color: #e8e7c5;

        &:hover {
          background-color: #ececd5;
        }

        &:active {
          background-color: #eae9ab;
        }
      }

      #reset-button {
        background-color: #bde1be;

        &:hover {
          background-color: #cce5cc;
        }

        &:active {
          background-color: #aed9af;
        }
      }
    }

    .b-room-list {
      margin: 10px 30px;
    }
  }
}
</style>
