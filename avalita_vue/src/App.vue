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
        >
        <div class="navbar-end">
          <router-link to="/dpto/fund" class="navbar-item">FUND</router-link>
          <router-link to="/dpto/aer" class="navbar-item">AER</router-link>
          <router-link to="/dpto/ele" class="navbar-item">ELE</router-link>
          <router-link to="/dpto/mec" class="navbar-item">MEC</router-link>
          <router-link to="/dpto/civil" class="navbar-item">CIVIL</router-link>
          <router-link to="/dpto/comp" class="navbar-item">COMP</router-link>
          <router-link to="/dpto/aesp" class="navbar-item">AESP</router-link>

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
export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>