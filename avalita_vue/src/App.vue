<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"
          ><strong>Avalita</strong></router-link
        >

        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>

          <span aria-hidden="true"></span>

          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link
            v-for="dpto in departamentos"
            :key="dpto.id"
            :to="dpto.get_absolute_url"
            class="navbar-item"
            >{{
              get_slug_from_url(dpto.get_absolute_url).toUpperCase()
            }}</router-link
          >

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light"
                >Log in</router-link
              >

              <router-link to="/aluno" class="button is-success">
                <span class="icon"><i class="fas fa-graduation-cap"></i></span>

                <span>Área do Aluno</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showMobileMenu: false,
      departamentos: [],
    };
  },
  mounted() {
    this.getAllDepartamentos();
  },
  methods: {
    async getAllDepartamentos() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/all-departamentos/")
        .then((response) => {
          this.departamentos = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
    get_slug_from_url(url) {
      return url.substring(6, url.length - 1);
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>