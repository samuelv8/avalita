<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="email"
      label="Email"
      required
    ></v-text-field>

    <v-text-field
      v-model="password"
      label="Password"
      required
      visibility_off
    ></v-text-field>

    <v-btn
      color="primary"
      class="mr-4"
      @click="printar_email"
    >
      Entrar
    </v-btn>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    email: '',
    password: '',
  }),
  methods: {
    printar_email () {
      console.log('email is: ' + this.email)
    },
  },
  name: "entrar",
  head() {
    const title = "Entrar"
    return {
      title
    }
  },
}
</script>

<style scoped>

</style>
