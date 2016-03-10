/* global window */
window.jQuery = window.$ = require('jquery');

const $ = window.$;

require('bootstrap');
require('bootstrap-datepicker');
require('bootstrap-datepicker/dist/locales/bootstrap-datepicker.pt-BR.min.js');
require('jquery.maskedinput/src/jquery.maskedinput.js');

$(() => {
  if ($('body').hasClass('account-personal-edit-data')) {
    $('.datepicker').datepicker({
      format: 'dd/mm/yyyy',
      todayBtn: 'linked',
      language: 'pt-BR',
      autoclose: true,
      defaultViewDate: { year: 1977, month: 10, day: 25 }
    });
    $('#id_cpf').mask('999.999.999-99');
    $('#id_cel').mask('(99) 99999-9999');
    $('#id_cep').mask('99999-999');
  } else if ($('body').hasClass('account account-condominium-list')) {
    $('#id_cnpj').mask('99.999.999/9999-99');
    $('#id_cep').mask('99999-999');
    $('#id_tel').mask('(99) 9999-9999');
  }
});
