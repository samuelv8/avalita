
<template>
  <div class="page-minha-conta">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Minha Conta</h1>
      </div>

      <div class="column is-12">
        <button @click="sair()" class="button is-danger">Sair</button>
      </div>

      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MyAccount",
  components: {},
  data() {
    return {};
  },
  mounted() {
    document.title = "Minha Conta | Avalita";
  },
  methods: {
    sair() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
};
</script>