<template>
  <div>
    <h1 class="subtitle">Nova avaliação</h1>
    <form @submit.prevent="submitForm">
      <div class="field">
        <label>Disciplina</label>
        <div class="control">
          <input type="text" class="input" v-model="disciplina" placeholder="ABC-12"/>
        </div>
      </div>

      <div class="field">
        <label>Nome do professor</label>
        <div class="control">
          <input type="text" class="input" v-model="professor" placeholder="Fulano de Tal"/>
        </div>
      </div>

      <div class="field">
        <label>Semestre em que você cursou a eletiva</label>
        <div class="control">
          <input type="text" class="input" v-model="ano" placeholder="2020.1"/>
        </div>
      </div>

      <div class="field">
        <label>Nota dada a essa eletiva com o respectivo professor</label>
        <div class="control">
          <select v-model="nota">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select>
        </div>
      </div>
    </form>
    <div class="column is-12">
      <button class="button is-dark mr-5" @click="submitForm()">
        Submeter avaliação
      </button>
      <router-link to="/area_aluno" class="button is-dark">
        <span>Retornar</span>
      </router-link>
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
      email: "alguem.alguem@ga.ita.br",
      disciplina: "",
      professor: "",
      ano: "",
      nota: "",
    };
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "Token " + this.$store.state.token;
      const formData = {
        "disciplina": this.disciplina,
        "professor": this.professor,
        "semestre_cronologico": this.ano,
        "nota": this.nota
      };

      await axios
          .post('/api/v1/submit-avaliacao/', formData)
          .then((response) => {
            this.disciplina = response.data;
            this.$router.push('/area_aluno/');
            alert("Você Submeteu uma Avaliação!");
          })
          .catch((error) => {
            if (error.response) {
              console.log(error);
              if (error.response.status == 403) {
                alert("Avaliação já feita!");
              } else {
                alert(error);
              }
            }
          });
          
    },
  }
};
</script>