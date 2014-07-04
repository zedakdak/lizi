<!-- Panneau Supérieur -->
<div
	class="edgePanel"
    data-dojo-type="dijit/layout/ContentPane"
    data-dojo-props="region: 'top'">LiziFacturation

<!-- Bouton Client -->
<button id="boutonsynthese"></button>
<button id="boutonfacture"></button>
<button id="boutondevis"></button>
<button id="boutonclient"></button>
<button id="boutonproduit"></button>
<button id="boutonoptions"></button>

</div>

<script>
require(["dijit/form/Button", "dojo/domReady!"],
function(Button) {

		var button1 = new Button({
			label: "Synthèse",
			style: "font-size: 20px",
			class: "buttonleft",
			onClick: function(){document.location.href='/web/app_dev.php/client'}}, "boutonsynthese");
			button1.startup();

		var button2 = new Button({
			label: "Facture",
			style: "font-size: 20px",
			class: "button",
			onClick: function(){document.location.href='/web/app_dev.php/facture'}}, "boutonfacture");
			button2.startup();

		var button3 = new Button({
			label: "Devis",
			style: "font-size: 20px",
			class: "button",
			onClick: function(){document.location.href='/web/app_dev.php/client'}}, "boutondevis");
			button3.startup();

		var button4 = new Button({
			label: "Client",
			style: "font-size: 20px",
			class: "button",
			onClick: function(){document.location.href='/web/app_dev.php/client'}}, "boutonclient");
			button4.startup();

		var button5 = new Button({
			label: "Produit",
			style: "font-size: 20px",
			class: "button",
			onClick: function(){document.location.href='/web/app_dev.php/client'}}, "boutonproduit");
			button5.startup();

		var button6 = new Button({
			label: "Options",
			style: "font-size: 20px",
			class: "button",
			onClick: function(){document.location.href='/web/app_dev.php/client'}}, "boutonoptions");
			button6.startup();
});
</script>





