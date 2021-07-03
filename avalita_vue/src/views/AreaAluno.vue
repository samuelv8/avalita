<template>
  <div>
    <div class="page-minha-conta ml-6">
      <div class="columns is-multiline">
        <div class="column is-9">
          <h1 class="title">Área do Aluno</h1>
          <h1 class="subtitle">{{ usr.email }}</h1>
        </div>
        <div class="column is-3 has-text-right">
          <router-link to="/nova_avaliacao" class="button is-dark">
            <span class="icon"><i class="fas fa-plus"></i></span>
            <span>Nova Avaliação</span>
          </router-link>
        </div>
        <div
            class="column is-3"
            v-for="aval in usr.avals"
            v-bind:key="aval.id"
        >
          <div class="box">
            <div class="columns is-multiline is-vcentered">
              <div class="column is-9">
                <router-link :to="aval.disciplina.get_absolute_url" class="dos-guri"><h3 class="is-size-4">
                  {{
                    get_disciplina_slug_from_url(
                        aval.disciplina.get_absolute_url
                    ).toUpperCase()
                  }}
                </h3></router-link>


                <p class="is-size-6 has-text-grey">
                  Prof. <strong>{{ aval.professor.name }}</strong>
                </p>

                <p class="is-size-6 has-text-grey">
                  Nota: <strong>{{ aval.nota }}</strong>
                </p>
              </div>
              <div class="column is-3 has-text-centered">
                <!--                <div class="button">-->
                <span class="icon" @click="delAval(aval.id)"><i class="fas fa-trash"></i></span>
                <!--                </div>-->
              </div>
            </div>
          </div>
        </div>
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
      usr: {
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
    async delAval(id) {
      console.log(id);
      await axios.delete('/api/v1/delete-avaliacao/', { data: {"id": id} } );
      this.usr.avals = this.usr.avals.filter(i => i.id !== id)
    },
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
            console.log(response.data);
            this.usr.avals = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
    },
    get_disciplina_slug_from_url(url) {
      const arr = url.split("/");
      const slug = arr[arr.length - 1];
      return slug;
    },
  },
};
</script>

<style scoped>
a.dos-guri:link {
  color: black;
  background-color: transparent;
  text-decoration: none;
}

a.dos-guri:visited {
  color: black;
  background-color: transparent;
  text-decoration: none;
}

a.dos-guri:hover {
  color: black;
  background-color: transparent;
  text-decoration: underline;
}

a.dos-guri:active {
  color: black;
  background-color: transparent;
  text-decoration: underline;
}
</style>
