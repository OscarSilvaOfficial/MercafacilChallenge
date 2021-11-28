<template>
  <div class="list">
    <h2 class='logo font-rem d-flex justify-center align-center' style='color: red; font-size: 6rem'>R&MFlix</h2>
    <vueper-slides
      ref="vueperslides1"
      v-if="showCharacters"
      slide-multiple
      class="no-shadow mt-11"
      :visible-slides="6"
      :bullets="false"
      :arrows="false"
      :slide-ratio="2 / 14"
      :dragging-distance="70">
      <vueper-slide 
        :style="getStyles(character.image)" 
        class="bg-screen" 
        v-for="(character, i) in characters" 
        :key="i"
      >
        <template #content>
          <div @mouseover="setCharacterDetails(character)" @mouseleave="closeCharacterDetails()" style="width: 100%; height: 100%"></div>
        </template>
      </vueper-slide>
    </vueper-slides>
    <Card :character="selectedCharacter" v-if="showCharacterDetails" />
  </div>
</template>

<script lang='ts'>
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore: Unreachable code error
import { VueperSlides, VueperSlide } from 'vueperslides'
import { Component, Vue } from 'vue-property-decorator';
import { GraphQLService } from '@/services/graphql'
import { ICharacter } from '@/intefaces/characters'
import { CHARACTERS } from './queries'
import Card from '@/views/characters/Card.vue'

@Component({
  components: { VueperSlides, VueperSlide, Card },
})
export default class Characters extends Vue {

  graphql = new GraphQLService()
  characters?: ICharacter[]
  selectedCharacter?: ICharacter | null
  showCharacters = false
  showCharacterDetails = false

  async created(): Promise<void> {
    const response: any = await this.graphql.get(CHARACTERS)
    this.characters = await response.data.data.characters.results
    this.showCharacters = true
  }

  setCharacterDetails(character: ICharacter): void {
    console.log(character)
    this.selectedCharacter = character
    this.showCharacterDetails = true
  }

  closeCharacterDetails(): void {
    this.showCharacterDetails = false
  }

  getStyles(image: string): string {
    return `background-image: url(${image}); background-size: contain;`
  }
}
</script>

<style lang="scss">
.logo {
  margin-top: 0;
}
.bg-screen {
  transition: all .5s;
  opacity: .3;
  &:hover {
    transform: scale(1.1);
    opacity: 1;
    width: 200px;
  }
}
</style> 
