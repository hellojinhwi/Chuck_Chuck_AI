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

<!-- Title  -->
<title>척척약사</title>

<!-- Favicon  -->
<link rel="icon" href="img/core-img/favicon.ico">

<!-- Style CSS -->
<link rel="stylesheet" href="style.css">

</head>

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

	<div class="featured-properties-area section-padding-100-50" id="textSearch">
		<div class="container pt-5">
			<div class="col-12">
				<div class="section-heading wow fadeInUp">
					<h2>의약품 식별 검색</h2>
				</div>
			</div>
		</div>
	</div>

	<!-- ##### Advance Search Area Start ##### -->
	<div class="south-search-area">
		<div class="container pb-5">
			<div class="row">
				<div class="col-12">
					<div class="advanced-search-form">
						<!-- Search Title -->
						<div class="search-title">
							<p>Search for your pill</p>
						</div>
						<!-- Search Form -->
						<form action="/textresult" id="advanceSearch">
							<div class="row">
								<div class="col-12 col-md-4">
									<div class="form-group">
										<input id="searchInput" autocomplete="on" type="text"
											class="form-control" name="name" placeholder="제품명">
									</div>
								</div>

								<div class="col-12 col-md-4">
									<div class="form-group">
										<input type="text" class="form-control" name="print1"
											placeholder="식별문자 1">
									</div>
								</div>

								<div class="col-12 col-md-4">
									<div class="form-group">
										<input type="text" class="form-control" name="print2"
											placeholder="식별문자 2">
									</div>
								</div>

								<div class="col-12 search-form-second-steps">
									<div class="row">
										<div class="col-12 col-md-4">
											<div class="form-group">
												<select id="social" class="form-control" name="shape">
													<option value="">모양</option>
													<option value="원형">원형</option>
													<option value="타원형">타원형</option>
													<option value="장방형">장방형</option>
													<option value="반원형">반원형</option>
													<option value="삼각형">삼각형</option>
													<option value="사각형">사각형</option>
													<option value="마름모형">마름모형</option>
													<option value="오각형">오각형</option>
													<option value="육각형">육각형</option>
													<option value="팔각형">팔각형</option>
													<option value="기타">기타</option>
												</select>
											</div>
										</div>

										<div class="col-12 col-md-4">
											<div class="form-group">
												<select class="form-control" name="color">
													<option value="">색상</option>
													<option value="하양">하양</option>
													<option value="노랑">노랑</option>
													<option value="주황">주황</option>
													<option value="분홍">분홍</option>
													<option value="빨강">빨강</option>
													<option value="갈색">갈색</option>
													<option value="연두">연두</option>
													<option value="초록">초록</option>
													<option value="청록">청록</option>
													<option value="파랑">파랑</option>
													<option value="남색">남색</option>
													<option value="자주">자주</option>
													<option value="보라">보라</option>
													<option value="회색">회색</option>
													<option value="검정">검정</option>
													<option value="투명">투명</option>
												</select>
											</div>
										</div>

									</div>
								</div>

								<div
									class="col-12 d-flex justify-content-between align-items-end">
									<!-- More Filter -->
									<div class="more-filter">
										<a href="#" id="moreFilter">+ More filters</a>
									</div>
									<!-- Submit -->
									<div class="form-group mb-0">
										<input type="submit" class="btn south-btn" value="검색">
									</div>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
	<!-- ##### Advance Search Area End ##### -->

	<script>

		var $j = jQuery.noConflict();
			
		$j(function() {    //화면 다 뜨면 시작
        	axios.get("http://localhost:8000/json")
        		.then(resdata => {
        			console.log(resdata.data)
        			
        			$j("#searchInput").autocomplete({
        				source : function(request, response) {
        			        var results = $j.ui.autocomplete.filter(resdata.data, request.term);
        			        response(results.slice(0, 10));
        				},
            			select : function(event, ui) {    //아이템 선택시
                		console.log(ui.item);
						},
						focus : function(event, ui) {    //포커스 가면
        					return false;//한글 에러 잡기용도로 사용됨
						},
						matchContains: true,
						minLength: 1,
        				autoFocus: true, //첫번째 항목 자동 포커스 기본값 false
        				classes: {    //잘 모르겠음
        					"ui-autocomplete": "highlight"
        				},
        				close : function(event){    //자동완성창 닫아질때 호출
        				console.log(event);
        				}})
				});
    	});
</script>



	<!-- ##### Featured Properties Area Start ##### -->
	

	<!-- ##### Call To Action Area Start ##### -->

	<!-- ##### Footer Area End ##### -->
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