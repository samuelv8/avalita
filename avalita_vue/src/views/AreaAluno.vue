<template>
  <div>
    <div class="page-minha-conta ml-6">
      <div class="columns is-multiline" v-if="semestre_atual == -1">
        <div class="column is-12">
          <h1 class="title">Área do Aluno</h1>
          <h1 class="subtitle">{{ email }}</h1>
          <router-link to="/nova_avaliacao" class="button is-dark">
            <span class="icon"><i class="fas fa-plus"></i></span>
            <span>Nova Avaliação</span>
          </router-link>
        </div>

        <div class="column is-6">
          <h1 class="subtitle">FUND</h1>
          <div class="column is-12">
            <button class="button is-dark mr-5" @click="setSemestre(1)">
              1º FUND - 1º semestre
            </button>
            <button class="button is-dark mr-5" @click="setSemestre(2)">
              1º FUND - 2º semestre
            </button>
          </div>

          <div class="column is-12">
            <button class="button is-dark mr-5" @click="setSemestre(3)">
              2º FUND - 1º semestre
            </button>
            <button class="button is-dark mr-5" @click="setSemestre(4)">
              2º FUND - 2º semestre
            </button>
          </div>
        </div>

        <div class="column is-6">
          <h1 class="subtitle">PROF</h1>
          <div class="column is-12">
            <button class="button is-dark mr-5" @click="setSemestre(5)">
              1º PROF - 1º semestre
            </button>
            <button class="button is-dark mr-5" @click="setSemestre(6)">
              1º PROF - 2º semestre
            </button>
          </div>

          <div class="column is-12">
            <button class="button is-dark mr-5" @click="setSemestre(7)">
              2º PROF - 1º semestre
            </button>
            <button class="button is-dark mr-5" @click="setSemestre(8)">
              2º PROF - 2º semestre
            </button>
          </div>

          <div class="column is-12">
            <button class="button is-dark mr-5" @click="setSemestre(9)">
              3º PROF - 1º semestre
            </button>
            <button class="button is-dark mr-5" @click="setSemestre(10)">
              3º PROF - 2º semestre
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="columns is-multiline" v-if="semestre_atual != -1">
      <div class="column is-6">
        <li v-for="avaliacao in semestres[semestre_atual]" :key="avaliacao.id">
          Disciplina: {{ avaliacao.disciplina.slug }}|Prof:
          {{ avaliacao.professor.name }}|Nota:{{ avaliacao.nota }}
        </li>

        <h1 class="subtitle">Nova avaliação</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Disciplina (ex: AED-34)</label>
            <div class="control">
              <input type="text" class="input" v-model="disciplina" />
            </div>
          </div>

          <div class="field">
            <label>Nome do professor</label>
            <div class="control">
              <input type="text" class="input" v-model="professor" />
            </div>
          </div>

          <div class="field">
            <label>Semestre em que você cursou a eletiva (ex: 2020.1)</label>
            <div class="control">
              <input type="text" class="input" v-model="ano" />
            </div>
          </div>

          <div class="field">
            <label>Nota dada a essa eletiva com o respectivo professor</label>
            <div class="control">
              <select class="input" v-model="nota">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </form>
      </div>
      <div class="column is-12">
        <button class="button is-dark mr-5" @click="submitForm()">
          Submeter avaliação
        </button>
        <button class="button grey mr-5" @click="setSemestre(-1)">
          Retornar
        </button>
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
      email: "alguem.alguem@ga.ita.br",
      semestres: [],
      semestre_atual: -1,
      disciplina: "",
      professor: "",
      ano: "",
      nota: "",
    };
  },
  mounted() {
    document.title = "Área do Aluno | Avalita";
    this.getData();
    this.getSemesters();
  },
  methods: {
    async getData() {
      axios.defaults.headers.common["Authorization"] =
        "Token " + this.$store.state.token;
      const response = await axios.get("/api/v1/users/me/");
      this.email = response.data.email;
    },
    async getSemesters() {
      axios.defaults.headers.common["Authorization"] =
        "Token " + this.$store.state.token;
      const response = await axios.get("/api/v1/my-semesters/");
      this.semestres = [null];
      for (let i = 1; i <= 10; i++) this.semestres.push(response.data[i] || []);
    },
    setSemestre(semestre) {
      this.semestre_atual = semestre;
    },
    async submitForm() {
      axios.defaults.headers.common["Authorization"] =
        "Token " + this.$store.state.token;
      const formData = {
        disciplina: this.disciplina,
        professor: this.professor,
        semestre_ita: this.semestre_atual,
        semestre_cronologico: this.ano,
        nota: this.nota,
      };
      try {
        await axios.post("/api/v1/submit-avaliacao/", formData);
        alert("Avaliação enviada");
      } catch (error) {
        alert("Erro encontrado");
      }
    },
  },
};
</script>

