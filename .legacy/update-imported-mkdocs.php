<?php
$authority_level = 'S';
$section		 = "tools";
include( __DIR__ . '/include/check-authority.php'); // Check for Authorization for Current Page.

include('include/functions-import.php');

// To get a particular tag value...
function get_tag_value($html='', $tag_name='')
{
	$_array	= array();
	if($html==''||$tag_name==''){
		return $_array;
	}
	// Use PHP DOMDocument class...
	if(class_exists('DOMDocument')){
		$dom = new DOMDocument;
		$dom->loadHTML($html);
		$_array = $dom->getElementsByTagName($tag_name);
	}
	return $_array;
}

?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=9; IE=8; IE=EDGE" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
	<link rel="shortcut icon" href="images/favicon.png" type="image/png">
	<title>Update MkDocs articles - PHPKB Knowledge Base Software</title>
	<!-- Bootstrap Select Plugin -->
	<link href="js/select/css/bootstrap-select.css" rel="stylesheet" type="text/css">
	
	<link href="css/style.default.css?v1.0.2" rel="stylesheet">
	<link href="css/phpkb.css?v=1.0.0" rel="stylesheet">
	<?php initCsrfVar4Js(); // Initializes a global CSRF variable to handle JS calls ?>
	

</head>
<body class="stickyheader">
	<!-- Preloader -->
	<div id="preloader">
		<div id="status"><i class="fa fa-spinner fa-spin"></i></div>
	</div>
	
	<!-- Language Switcher - STARTS -->
	<?php include_once('language-switcher.php'); ?>
	<!-- Language Switcher - ENDS -->
	
	<section>
		<div class="leftpanel">
			<!-- Logo Panel - STARTS -->
			<?php include_once('logo.php'); ?>
			<!-- Logo Panel - ENDS -->
			
			<!-- Left Panel - STARTS -->
			<?php include_once('menu.php'); ?>
			<!-- Left Panel - ENDS -->
		</div>
		
		<div class="mainpanel">
			
			<!-- Header - STARTS -->
			<?php include_once('header.php'); ?>
			<!-- Header - ENDS -->
			
			<div class="pageheader">
				<h2><i class="fa fa-arrow-circle-down"></i> Update MkDocs articles</h2>
				<div class="breadcrumb-wrapper">
					<span class="label">You are here:</span>
					<ol class="breadcrumb">
						<li>Tools</li>
						<li>Update imported MkDocs articles</li>
					</ol>
				</div>
			</div>
			
			<div class="contentpanel">
				<?php echo $display_message.
				"<p align=\"justify\" class=\"{$hidden_xs}{$visible_sm}{$visible_md}{$visible_lg}\">
					Update Imported MkDocs articles in the knowledge base.
				</p>";
				 ?>
				 <div class="row">
					<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
						<ul class="nav nav-tabs nav-info item-color tabs-stacked">
                            <li class="active"><a href="update-imported-mkdocs.php"><i class="fa fa-cloud-download"></i> &nbsp;Update MkDocs</a></li>
						</ul>
					</div>
				</div>
				<div class="tab-content mb30">
					<div class="row">
						<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
							<form name="frmimporthtml" action="import-html.php" method="post" class="form-horizontal">
								<div class="panel panel-default mt10 mr10 ml10">
									<div class="panel-heading">
										<div class="panel-btns">
											<a href="javascript:;" class="minimize">&minus;</a>
										</div>
										<h4 class="panel-title">Update MkDocs articles <?php echo $current_language; ?></h4>
									</div>
									<div class="panel-body<?php echo $noPadding ; ?>">
										<div id="html_output">
											<?php
											echo'<div style="padding:10px;">TODO write the href parser.</div>';
                                            $article_title = 'Импорт из справочной системы';
                                            $sql_result = mysqli_query($GLOBALS['connection'], "SELECT article_id, article_title, article_content FROM phpkb_articles WHERE article_title LIKE '%$article_title' {$AND_Language_Query}");
                                            
                                            while ($entry = $sql_result->fetch_array(MYSQLI_ASSOC))
                                            {
                                            $article_id = $entry ['article_id'];
                                            $article_title = $entry ['article_title'];
                                            $article_content = htmlspecialchars_decode($entry ['article_content'],  ENT_QUOTES | ENT_SUBSTITUTE);
                                            echo "<div style=\"padding:10px;\">Article ID: $article_id, title: $article_title</div>";
                                            echo "<div style=\"padding:10px;\">Article content:</div>";
                                            echo "<div style=\"padding:10px;\">$article_content</div>";
                                            echo "<div style=\"padding:10px;\">Article links:</div>";
                                            foreach (get_tag_value($article_content, 'a') as $article_link)
                                            {
                                            $link_text = utf8_decode($article_link->nodeValue);
                                            $href = utf8_decode($article_link->getAttribute('href'));
                                            echo "<div style=\"padding:10px;\">$link_text</div>";
                                            echo "<div style=\"padding:10px;\">$href</div>";
                                            }
                                            }
											 ?>
										</div>
									</div>
								</div>
							</form>
						</div>
					</div><!--row -->
				</div>
			</div>
			<div class="padding5 text-center poweredby">
				Powered by <a href="http://www.knowledgebase-script.com" target="_blank">PHPKB Knowledge Base Software</a> 
				<span class="xs-poweredby">&copy; <?php echo '2005-'.date('Y'); ?> <a href="http://www.chadhasoftware.com" target="_blank">Chadha Software Technologies</a></span>
			</div>
		</div><!-- mainpanel -->
		
		<!-- Right Panel - STARTS -->
		<?php include_once('right-panel.php'); ?>
		<!-- Right Panel - ENDS -->
	
	</section>
	
	<!-- JavaScript -->
	<script src="js/jquery-1.11.1.min.js"></script>
	<script src="js/jquery-migrate-1.2.1.min.js"></script>
	<script src="js/jquery-ui-1.10.3.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/modernizr.min.js"></script>
	
	<script src="js/toggles.min.js"></script>
	
	<!-- Bootstrap Select Plugin -->
	<script src="js/select/js/bootstrap-select.js" type="text/javascript"></script>
	
	<script src="js/jquery.cookies.js"></script>
	<script src="js/jquery.validate.min.js"></script>
	<?php initJsLefMenuParam(); ?>
	<script src="js/custom.js?v=1.0.3"></script>
	
	<script src="js/common.js?v=1.0.0" type="text/javascript"></script>
	<script src="js/articles.js?v=1.0.0" type="text/javascript"></script>
	<script src="js/import-html.js" type="text/javascript"></script>
	<script type="text/javascript">
	jQuery(document).ready(function(){
		"use strict";
		
	});
	</script>
	
<?php db_disconnect($GLOBALS['connection']); ?>
</body>
</html>