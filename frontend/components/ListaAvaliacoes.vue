<template>
  <v-container fluid>

    <AvaliacaoIndividual v-for="aval in numAval" :key="aval"></AvaliacaoIndividual>

  </v-container>
</template>

<script>
import AvaliacaoIndividual from "@/components/AvaliacaoIndividual";
export default {
  name: "ListaAvaliacoes",
  data () {
    return {
      numAval: 5,
    }
  },
  components: {
    AvaliacaoIndividual,
  }
}
</script>

<style scoped>

</style>
