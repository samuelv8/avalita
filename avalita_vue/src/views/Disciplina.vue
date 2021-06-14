<template>
  <div class="page-product">
    <h1 class="title">
      <strong v-if="disciplina.get_absolute_url">
        {{
          get_disciplina_slug_from_url(
            disciplina.get_absolute_url
          ).toUpperCase()
        }}
      </strong>
      - {{ disciplina.name }}
    </h1>

    <li
      v-for="media in medias"
      v-bind:key="(media.disciplina.id, media.professor.id)"
    >
      Nota: <strong> {{ media.nota }} </strong>/5.00 |
      <span>
        {{ media.count }} {{ media.count == 1 ? "avaliação" : "avaliações" }}
      </span>
      |
      <span>
        <router-link :to="media.professor.get_absolute_url">
          Prof. {{ media.professor.name }}
        </router-link>
      </span>
    </li>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Disciplina",
  data() {
    return {
      disciplina: {},
      medias: [],
    };
  },
  mounted() {
    this.getDisciplina();
    this.getMedias();
  },
  methods: {
    async getMedias() {
      this.$store.commit("setIsLoading", true);
      const departamento_slug = this.$route.params.departamento_slug;
      const disciplina_slug = this.$route.params.disciplina_slug;
      await axios
        .get(`/api/v1/best-medias/${departamento_slug}/${disciplina_slug}`)
        .then((response) => {
          this.medias = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async getProfessores() {
      this.$store.commit("setIsLoading", true);
      const departamento_slug = this.$route.params.departamento_slug;
      const disciplina_slug = this.$route.params.disciplina_slug;
      await axios
        .get(`/api/v1/dpto/${departamento_slug}/${disciplina_slug}/p`)
        .then((response) => {
          this.professores = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async getDisciplina() {
      this.$store.commit("setIsLoading", true);
      const departamento_slug = this.$route.params.departamento_slug;
      const disciplina_slug = this.$route.params.disciplina_slug;
      await axios
        .get(`/api/v1/dpto/${departamento_slug}/${disciplina_slug}`)
        .then((response) => {
          this.disciplina = response.data;
          document.title = this.disciplina.name + " | Avalita";
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    get_disciplina_slug_from_url(url) {
      const arr = url.split("/");
      const slug = arr[arr.length - 1];
      return slug;
    },
  },
};
</script>