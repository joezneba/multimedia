(function($) {

  $.fn.menumaker = function(options) {
      
      var cssmenu = $(this), settings = $.extend({
        title: "Menu",
        format: "dropdown",
        sticky: false
      }, options);

      return this.each(function() {
        cssmenu.prepend('<div id="menu-button">' + settings.title + '</div>');
        $(this).find("#menu-button").on('click', function(){
          $(this).toggleClass('menu-opened');
          var mainmenu = $(this).next('ul');
          if (mainmenu.hasClass('open')) { 
            mainmenu.hide().removeClass('open');
          }
          else {
            mainmenu.show().addClass('open');
            if (settings.format === "dropdown") {
              mainmenu.find('ul').show();
            }
          }
        });

        cssmenu.find('li ul').parent().addClass('has-sub');

        multiTg = function() {
          cssmenu.find(".has-sub").prepend('<span class="submenu-button"></span>');
          cssmenu.find('.submenu-button').on('click', function() {
            $(this).toggleClass('submenu-opened');
            if ($(this).siblings('ul').hasClass('open')) {
              $(this).siblings('ul').removeClass('open').hide();
            }
            else {
              $(this).siblings('ul').addClass('open').show();
            }
          });
        };

        if (settings.format === 'multitoggle') multiTg();
        else cssmenu.addClass('dropdown');

        if (settings.sticky === true) cssmenu.css('position', 'fixed');

        resizeFix = function() {
          if ($( window ).width() > 768) {
            cssmenu.find('ul').show();
          }

          if ($(window).width() <= 768) {
            cssmenu.find('ul').hide().removeClass('open');
          }
        };
        resizeFix();
        return $(window).on('resize', resizeFix);

      });
  };
})(jQuery);

var ip_cliente = 0;

(function($){
    $(document).ready(function(){

        $("#cssmenu").menumaker({
            title: "Menu",
            format: "multitoggle"
        });

        /*----- VERIFICAR SI EL USUARIO ESTÁ LOGUEADO -----*/
        if (user_auth === 'True') {
            comprobarPerfil();
            getIP ();
        }

        /*----- VERIFICAR SI EXISTE LA VARIABLE REGISTRO -----*/
        if (typeof registro !== 'undefined'){
            getIP ();
        }

        /*----- FUNCIÓN BÚSQUEDA DE VIDEOS -----*/
        $('#buscarVideo').keyup(function (e) {
            consulta = $('#buscarVideo').val();
            $.ajax({
                data: {'nombre': consulta},
                url: '/video/busqueda_video',
                type: 'get',
                success: function (data) {
                    console.log(data);

                    var finalData =$.map(data, function(item) {
                        return {
                            label:item.nombre,
                            value:item.nombre,
                            pk: item.pk
                        }
                    });

                    console.log('FinalData', finalData);

                    $("#buscarVideo").autocomplete({
                        source: finalData,
                        select: function(event, ui) {
                            var pk = ui.item.pk;
                            document.location.href = url.replace('123', pk);
                        }
                    });
                },
                error: function (message) {
                    console.log(message);
                }
            })
        });

    });
})(jQuery);

/*----- FUNCIÓN PARA COMPROBAR SI EL USUARIO TIENE PERFIL -----*/
function comprobarPerfil() {
    var resp = true;
    $.ajax({
        type: 'get',
        url: '/usuario/comprobarPerfil',
        success: function (res) {
            resp = res;

            if (res === 'False') {
                $('#dialog').dialog({
                    modal: true,
                    dialogClass: "no-close",
                    show: { effect: "blind", duration: 800 }
                });
            }
        }
    });
}

/*----- FUNCIÓN PARA GUARDAR UN NUEVO PERFIL -----*/
function guardarPefil() {
    var cedula = $('#cedula').val();
    var telefono = $('#telefono').val();
    var fecha_nacimiento = $('#fecha_nac').val();

    $.ajax({
        url: '/usuario/crearPerfil',
        type: 'POST',
        data: {
            'cedula' : cedula,
            'telefono' : telefono,
            'fecha_nacimiento' : fecha_nacimiento,
            'ip_cliente' : ip_cliente,
            'csrfmiddlewaretoken': token
        },
        success: function (res) {
            $('#dialog').dialog( "close" );
        }
    })
}

/*----- FUNCIÓN PARA OBTENER LA IP DEL USUARIO -----*/
function getIP() {
    $.getJSON('//freegeoip.net/json/?callback=?', function(data) {
        ip_cliente = data.ip;
        console.log(ip_cliente);
        $('input[name=ip_registro]').val(ip_cliente);
    });
}

