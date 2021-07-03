<template>
  <div class="home">
    <section class="hero is-small is-dark mb-6">
      <div class="hero-body has-text-centered">
        <img src="https://i.imgur.com/HrV8xwb.png" alt="logotipo do avalita"/>
        <p class="title mb-5 mt-4">Bem-vindo(a) ao Avalita</p>
        <p class="subtitle">Eletivas avaliadas por iteanos</p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered is-capitalized">
          Melhores Avaliações
        </h2>
      </div>

      <div
          class="column is-3"
          v-for="media in medias"
          v-bind:key="(media.disciplina.id, media.professor.id)"
      >
        <div class="box">
          <h3 class="is-size-4">
            {{
              get_disciplina_slug_from_url(
                  media.disciplina.get_absolute_url
              ).toUpperCase()
            }}
          </h3>

          <p class="is-size-6 has-text-grey">
            Prof. <strong>{{ media.professor.name }}</strong>
          </p>

          <p class="is-size-6 has-text-grey">
            Nota: <strong>{{ media.nota }}</strong> ({{ media.count }}
            {{ media.count == 1 ? "avaliação" : "avaliações" }})
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      medias: [],
    };
  },
  mounted() {
    document.title = "Home | Avalita";
    this.getMedias();
  },
  methods: {
    async getMedias() {
      this.$store.commit("setIsLoading", true);
      await axios
          .get("/api/v1/best-medias/")
          .then((response) => {
            this.medias = response.data;
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
  components: {},
};
</script>