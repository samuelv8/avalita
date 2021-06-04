<template>
  <v-app>
    <v-app-bar
      app
      min-height="80"
      color="white"
    >
      <v-card
        nuxt
        to="/departamentos"
        flat
        :ripple="true"
        v-click-outside=""
      >
        <v-img
          max-height="200"
          max-width="240"
          src="https://user-images.githubusercontent.com/24798860/119005862-3318d400-b966-11eb-865a-6c22fb983c7c.png"
        ></v-img>
      </v-card>
      <v-spacer/>
      <v-card-text>
        Você tá logado!
      </v-card-text>
      <v-spacer/>
      <v-card
        nuxt
        to="/area-aluno"
        flat
      >
        <v-icon x-large>
          mdi-account
        </v-icon>
      </v-card>
    </v-app-bar>
    <v-main>
      <v-content>
        <v-container fluid>
          <Nuxt/>
        </v-container>
      </v-content>
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
