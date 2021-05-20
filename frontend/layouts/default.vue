<template>
  <v-app>
    <v-app-bar
      fixed
      app
    >
      <v-img
        max-height="150"
        max-width="250"
        src="https://user-images.githubusercontent.com/24798860/119005862-3318d400-b966-11eb-865a-6c22fb983c7c.png"
      ></v-img>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt/>
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
