<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="description" content="">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport"
	content="width=device-width, initial-scale=1, shrink-to-fit=no">
<!-- The above 4 meta tags *must* come first in the head; any other head content must come *after* these tags -->

<!-- 자동완성 스타일시트 -->
<link rel="stylesheet"
	href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script src="assets/js/axios.js"></script>
<link rel="stylesheet"
	href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
	integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
	crossorigin="anonymous">


<!-- Title  -->
<title>척척약사</title>

<!-- Favicon  -->
<link rel="icon" href="img/core-img/favicon.ico">

<!-- Style CSS -->
<link rel="stylesheet" href="style.css">

</head>
<style>
.filebox {
	display: inline-block;
	padding: .5em .75em;
	color: #fff;
	font-size: 1.7em;
	line-height: normal;
	vertical-align: middle;
	background-color: #947054;
	cursor: pointer;
	border: 1px solid #947054;
	border-radius: .25em;
	-webkit-transition: background-color 0.2s;
	transition: background-color 0.2s;
}

.filebox :hover {
	background-color: #000000;
}

.filebox :active {
	background-color: #000000;
}
</style>
<body>




	<!-- Preloader -->
	<div id="preloader">
		<div class="south-load"></div>
	</div>

	<!-- ##### Header Area Start ##### -->
	<header class="header-area">

		<!-- Main Header Area -->
		<div class="main-header-area" id="stickyHeader">
			<div class="classy-nav-container breakpoint-off">
				<!-- Classy Menu -->
				<nav class="classy-navbar justify-content-between" id="southNav">

					<!-- Logo -->
					<a class="nav-brand" href="index"><img
						src="img/core-img/logo.png" align="middle"> 척척약사</a>


					<!-- Navbar Toggler -->
					<div class="classy-navbar-toggler">
						<span class="navbarToggler"><span></span><span></span><span></span></span>
					</div>

					<!-- Menu -->
					<div class="classy-menu">

						<!-- close btn -->
						<div class="classycloseIcon">
							<div class="cross-wrap">
								<span class="top"></span><span class="bottom"></span>
							</div>
						</div>

						<!-- Nav Start -->
						<div class="classynav">
							<ul>
								<li><a href="http://localhost:8000/">텍스트 검색</a></li>
								<li><a href="http://localhost:5000/">이미지 검색</a></li>
							</ul>



						</div>
						<!-- Nav End -->
					</div>
				</nav>
			</div>
		</div>
	</header>
	<!-- ##### Header Area End ##### -->



	<br>
	<br>
	<br>
	<!-- ##### Featured Properties Area Start ##### -->
	<section class="featured-properties-area section-padding-100-50">
		<div class="container pt-5">
			<div class="row">
				<div class="col-12">
					<div class="section-heading wow fadeInUp">
						<h2>검색한 결과가 없습니다.</h2>
						<p>다시 검색해 주시기 바랍니다.</p>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!-- ##### Featured Properties Area End ##### -->
	<!-- Start Sample Area -->


	<div class="south-search-area">
		<div class="container pb-5">
			<div class="row">
				<div class="col-md-6 px-5">
					<p align="center">
						<button class="filebox " onclick="location.href='/index'">텍스트
							검색</button>
					</p>
				</div>
				<div class="col-md-6 px-5">
					<p align="center">
						<!-- Search Title -->
						<button class="filebox" onclick="location.href='http://localhost:5000/'">이미지
							검색</button>
					</p>
				</div>
			</div>
		</div>
	</div>

	<!-- ##### Call To Action Area End ##### -->




	<!-- ##### Editor Area End ##### -->

	<!-- ##### Footer Area Start ##### -->
	<footer
		class="footer-area section-padding-100-0 bg-img gradient-background-overlay"
		style="background-image: url(img/bg-img/cta.jpg);">
		<!-- Main Footer Area -->
		<div class="main-footer-area">
			<div class="container">
				<div class="row">

					<!-- Single Footer Widget -->
					<div class="col-12 col-sm-6 col-xl-3">
						<div class="footer-widget-area mb-100">
							<!-- Widget Title -->
							<div class="widget-title">
								<h6>About Us</h6>
							</div>

							<img src="img/bg-img/footer.jpg" alt="">
							<div class="footer-logo my-4">
								<img src="img/core-img/logo.png" alt="">
							</div>
							<p>Integer nec bibendum lacus. Suspen disse dictum enim sit
								amet libero males uada feugiat. Praesent malesuada.</p>
						</div>
					</div>

					<!-- Single Footer Widget -->
					<div class="col-12 col-sm-6 col-xl-3">
						<div class="footer-widget-area mb-100">
							<!-- Widget Title -->
							<div class="widget-title">
								<h6>Hours</h6>
							</div>
							<!-- Office Hours -->
							<div class="weekly-office-hours">
								<ul>
									<li class="d-flex align-items-center justify-content-between"><span>Monday
											- Friday</span> <span>09 AM - 19 PM</span></li>
									<li class="d-flex align-items-center justify-content-between"><span>Saturday</span>
										<span>09 AM - 14 PM</span></li>
									<li class="d-flex align-items-center justify-content-between"><span>Sunday</span>
										<span>Closed</span></li>
								</ul>
							</div>
							<!-- Address -->
							<div class="address">
								<h6>
									<img src="img/icons/phone-call.png" alt=""> +45 677
									8993000 223
								</h6>
								<h6>
									<img src="img/icons/envelope.png" alt="">
									office@template.com
								</h6>
								<h6>
									<img src="img/icons/location.png" alt=""> Main Str. no
									45-46, b3, 56832, Los Angeles, CA
								</h6>
							</div>
						</div>
					</div>

					<!-- Single Footer Widget -->
					<div class="col-12 col-sm-6 col-xl-3">
						<div class="footer-widget-area mb-100">
							<!-- Widget Title -->
							<div class="widget-title">
								<h6>Useful Links</h6>
							</div>
							<!-- Nav -->
							<ul class="useful-links-nav d-flex align-items-center">
								<li><a href="#">Home</a></li>
								<li><a href="#">About us</a></li>
								<li><a href="#">About us</a></li>
								<li><a href="#">Services</a></li>
								<li><a href="#">Properties</a></li>
								<li><a href="#">Listings</a></li>
								<li><a href="#">Testimonials</a></li>
								<li><a href="#">Properties</a></li>
								<li><a href="#">Blog</a></li>
								<li><a href="#">Testimonials</a></li>
								<li><a href="#">Contact</a></li>
								<li><a href="#">Elements</a></li>
								<li><a href="#">FAQ</a></li>
							</ul>
						</div>
					</div>

					<!-- Single Footer Widget -->
					<div class="col-12 col-sm-6 col-xl-3">
						<div class="footer-widget-area mb-100">
							<!-- Widget Title -->
							<div class="widget-title">
								<h6>Featured Properties</h6>
							</div>
							<!-- Featured Properties Slides -->
							<div class="featured-properties-slides owl-carousel">
								<!-- Single Slide -->
								<div class="single-featured-properties-slide">
									<a href="#"><img src="img/bg-img/fea-product.jpg" alt=""></a>
								</div>
								<!-- Single Slide -->
								<div class="single-featured-properties-slide">
									<a href="#"><img src="img/bg-img/fea-product.jpg" alt=""></a>
								</div>
								<!-- Single Slide -->
								<div class="single-featured-properties-slide">
									<a href="#"><img src="img/bg-img/fea-product.jpg" alt=""></a>
								</div>
							</div>
						</div>
					</div>

				</div>
			</div>
		</div>

		<!-- Copywrite Text -->
		<div
			class="copywrite-text d-flex align-items-center justify-content-center">
			<p>
				<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
				Copyright &copy;
				<script>
					document.write(new Date().getFullYear());
				</script>
				All rights reserved | This template is made with <i
					class="fa fa-heart-o" aria-hidden="true"></i> by <a
					href="https://colorlib.com" target="_blank">Colorlib</a>
				<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
		</div>
	</footer>
	<!-- ##### Footer Area End ##### -->

	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

	<script src="assets/js/jquery.min.js"></script>
	<script src="assets/js/jquery-migrate-3.0.1.min.js"></script>
	<script src="assets/js/popper.min.js"></script>
	<script src="assets/js/bootstrap.min.js"></script>
	<script src="assets/js/jquery.easing.1.3.js"></script>
	<script src="assets/js/jquery.waypoints.min.js"></script>
	<script src="assets/js/jquery.stellar.min.js"></script>
	<script src="assets/js/owl.carousel.min.js"></script>
	<script src="assets/js/jquery.magnific-popup.min.js"></script>
	<script src="assets/js/aos.js"></script>
	<script src="assets/js/jquery.animateNumber.min.js"></script>
	<script src="assets/js/bootstrap-datepicker.js"></script>
	<script src="assets/js/scrollax.min.js"></script>
	<script src="assets/js/main.js"></script>

	<!-- jQuery (Necessary for All JavaScript Plugins) -->
	<script src="js/jquery/jquery-2.2.4.min.js"></script>

	<!-- Popper js -->
	<script src="js/popper.min.js"></script>

	<!-- Bootstrap js -->
	<script src="js/bootstrap.min.js"></script>

	<!-- Plugins js -->
	<script src="js/plugins.js"></script>
	<script src="js/classy-nav.min.js"></script>
	<script src="js/jquery-ui.min.js"></script>

	<!-- Active js -->
	<script src="js/active.js"></script>



</body>

</html>