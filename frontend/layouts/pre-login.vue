<template>
  <v-app>
    <v-app-bar
      app
      min-height="80"
    >
      <v-img
        max-height="200"
        max-width="240"
        src="https://user-images.githubusercontent.com/24798860/119005862-3318d400-b966-11eb-865a-6c22fb983c7c.png"
      ></v-img>
      <v-spacer/>
      <v-btn
        color="primary"
        nuxt
        to="/registrar"
      >
        Registrar
      </v-btn>
      <v-btn
        color="primary"
        nuxt
        to="/entrar"
      >
        Login
      </v-btn>
    </v-app-bar>
    <v-spacer/>
    <v-main>
      <v-container>
        <Nuxt/>
      </v-container>
    </v-main>
    <v-footer
      :absolute="!fixed"
      app
    >
      <span>{{ title }} &copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      fixed: false,
      title: 'avalITA',
    }
  }
}
</script>
