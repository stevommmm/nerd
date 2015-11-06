/* Nav menu dropdown */
var PopOver = function(elementId) {
	this.e_parent = document.getElementById(elementId + "-parent");
	this.e_child = document.getElementById(elementId + "-child");
	this.e_close = document.getElementById(elementId + "-close");
};
PopOver.prototype.toggle = function() {
	this.e_child.style.display = this.e_child.style.display === "block" ? "none": "block";
	this.e_child.style.left = (this.e_parent.offsetWidth / 2) - (this.e_child.offsetWidth / 2) + "px";
};
PopOver.prototype.register = function() {
	this.e_parent.onclick = function(e) {
		e.preventDefault();
		this.toggle();
		e.stopImmediatePropagation();
	}.bind(this);
	this.e_close.onclick = function(e) {
		e.preventDefault();
		this.toggle();
		e.stopImmediatePropagation();
	}.bind(this);
};

/* Server name link copy selector */
var ClickCopy = function(elementId, address) {
	this.e_parent = document.getElementById(elementId);
	this.address = address;
};
ClickCopy.prototype.register = function() {
	this.e_parent.onclick = function(e) {
		this.e_parent.innerHTML = this.address;

		var selection = window.getSelection();            
        var range = document.createRange();
        range.selectNodeContents(this.e_parent);
        selection.removeAllRanges();
        selection.addRange(range);

        this.e_parent.onclick = function() {};
	}.bind(this);
};

/* skin render */