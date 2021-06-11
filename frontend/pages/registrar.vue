<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Nome"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

<!--    <v-select-->
<!--      v-model="select"-->
<!--      :items="items"-->
<!--      :rules="[v => !!v || 'Item is required']"-->
<!--      label="Item"-->
<!--      required-->
<!--    ></v-select>-->

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

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Você concorda?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!valid"
      color="primary"
      class="mr-4"
      @click="validate"
    >
      Registrar
    </v-btn>

    <v-btn
      color="primary"
      class="mr-4"
      @click="reset"
    >
      Limpar
    </v-btn>

    <v-btn
      color="primary"
      @click="resetValidation"
    >
      Cancelar
    </v-btn>
  </v-form>
</template>

<script>

export default {
  name: "index",
  layout: 'pre-login',
  head() {
    const title = "HomePage"
    return {
      title
    }
  },

  data: () => ({
    valid: true,
    name: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 10) || 'Name must be less than 10 characters',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    // select: null,
    // items: [
    //   'Item 1',
    //   'Item 2',
    //   'Item 3',
    //   'Item 4',
    // ],
    //checkbox: false,
    show3 : false,
    rules: {
      // required: value => !!value || 'Required.',
      // min: v => v.length >= 8 || 'Min 8 characters',
    },
  }),

  methods: {
    validate () {
      this.$refs.form.validate()
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
  },
}
</script>

<style scoped>

</style>
