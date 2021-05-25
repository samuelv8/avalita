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
      :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
      :rules="[rules.required, rules.min]"
      :type="show3 ? 'text' : 'password'"
      name="input-10-2"
      label="Senha"
      hint="At least 8 characters"
      v-model="password"
      class="input-group--focused"
      @click:append="show3 = !show3"
    ></v-text-field>

    <v-btn
      nuxt
      to="/departamentos"
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
    show3 : false,
    rules: {
      // required: value => !!value || 'Required.',
      // min: v => v.length >= 8 || 'Min 8 characters',
    },
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
