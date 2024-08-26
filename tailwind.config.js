module.exports = {
  mode: 'jit',
  content: ["./templates/**/*.{html,htm}"],
  theme: {
    extend: {
      backgroundColor:{
        'brand-blue' : '#64CEBB',
        'brand-yellow' : '#F5C645',
        'brand-red' : '#FE602F',
        'brand-purple' : 'E6C7EB',
      }
    },
  },
  plugins: [],
}