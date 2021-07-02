<template>
  <div>
    <div class="page-minha-conta ml-6">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h1 class="title">Área do Aluno</h1>
          <h1 class="subtitle">{{ usr.email }}</h1>
          <router-link to="/nova_avaliacao" class="button is-dark">
            <span class="icon"><i class="fas fa-plus"></i></span>
            <span>Nova Avaliação</span>
          </router-link>
        </div>
      </div>
      <div class="">

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AreaAluno",
  components: {},
  data() {
    return {
      usr : {
        email: "alguem.alguem@ga.ita.br",
        username: "alguem.alguem",
        avals: [],
      },
    };
  },
  mounted() {
    document.title = "Área do Aluno | Avalita";
    this.getData();
  },
  methods: {
    async getData() {
      axios.defaults.headers.common["Authorization"] =
        "Token " + this.$store.state.token;
      await axios
        .get("/api/v1/users/me/")
        .then((response) => {
          this.usr.email = response.data.email;
          this.usr.username = response.data.username;
        })
        .catch((error) => {
          console.log(error);
        });

      const requestAvals = {
        "user": this.username,
      };

      await axios
        .get(`/api/v1/my-avals/`, requestAvals)
        .then((response) => {
          this.usr.avals = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

