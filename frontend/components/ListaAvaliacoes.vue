<template>
  <v-container fluid>

    <AvaliacaoIndividual
      v-for="(aval, i) in avals" :key="i"
      v-bind:aval="aval"
    ></AvaliacaoIndividual>

  </v-container>
</template>

<script>
import AvaliacaoIndividual from "@/components/AvaliacaoIndividual";
export default {
  name: "ListaAvaliacoes",
  props: {
    avals: Array,
  },
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
