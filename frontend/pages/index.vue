<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
          Seja bem-vindo, iteano!
        </v-card-title>
        <v-card-text>
          <p>O objetivo da plataforma a seguir é compartilhar as experiências de quem já fez a eletiva com aqueles que
            estão pensando em fazê-la.</p>
          <p>Nessa plataforma, você pode:</p>
          <ul>
            <li>avaliar a cobrança da eletiva</li>
            <li>avaliar a pontualidade do professor</li>
            <li>avaliar se a melação era possível</li>
          </ul>
          <div class="text-xs-right">
            <em><small>&mdash; Time do avalITA</small></em>
          </div>
          <hr class="my-3">
          <p> Projeto da COMP-23 &mdash; 1º semestre </p>
          <p> Disciplina de CES-22 &mdash; prof. Karla Fook </p>
        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn
            color="primary"
            nuxt
            to="/registre"
          >
            Registre
          </v-btn>
          <v-btn
            color="primary"
            nuxt
            to="/entrar"
          >
            Entrar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "index",
  head() {
    const title = "HomePage"
    return {
      title
    }
  },
}
</script>
