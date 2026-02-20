resource "aws_s3_bucket" "mybucket" {
  bucket = var.mybucket
}

resource "aws_s3_bucket_ownership_controls" "example" {
  bucket = aws_s3_bucket.mybucket.id

  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.mybucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "example" {
  depends_on = [
    aws_s3_bucket_ownership_controls.example,
    aws_s3_bucket_public_access_block.example,
  ]

  bucket = aws_s3_bucket.mybucket.id
  acl    = "public-read"
}

resource "aws_s3_object" "index" {
  bucket = aws_s3_bucket.mybucket.id
  key    = "index.html"
  source = "file_sito/index.html"
  acl = "public-read"
  content_type = "text/html"
}

resource "aws_s3_object" "error" {
  bucket = aws_s3_bucket.mybucket.id
  key    = "error.html"
  source = "file_sito/error.html"
  acl = "public-read"
  content_type = "text/html"
}

resource "aws_s3_object" "chi-siamo" {
  bucket = aws_s3_bucket.mybucket.id
  key    = "chi-siamo.html"
  source = "file_sito/chi-siamo.html"
  acl = "public-read"
  content_type = "text/html"
}

resource "aws_s3_object" "collabora" {
  bucket = aws_s3_bucket.mybucket.id
  key    = "collabora.html"
  source = "file_sito/collabora.html"
  acl = "public-read"
  content_type = "text/html"
}

resource "aws_s3_object" "eventi" {
  bucket = aws_s3_bucket.mybucket.id
  key    = "eventi.html"
  source = "file_sito/eventi.html"
  acl = "public-read"
  content_type = "text/html"
}

resource "aws_s3_object" "materiale" {
  bucket = aws_s3_bucket.mybucket.id
  key    = "materiale.html"
  source = "file_sito/materiale.html"
  acl = "public-read"
  content_type = "text/html"
}

resource "aws_s3_object" "style" {
  bucket = aws_s3_bucket.mybucket.id
  key    = "style.css"
  source = "file_sito/style.css"
  acl = "public-read"
  content_type = "text/css"
}

resource "aws_s3_bucket_website_configuration" "example" {
  bucket = aws_s3_bucket.mybucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }

depends_on = [ aws_s3_bucket.mybucket ]

}