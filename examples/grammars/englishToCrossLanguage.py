englishToCrossLanguage = [
[["<<foo>> ;"], "(semicolon <<foo>>)", "final"],
[["<<foo>> { <<bar>> }"], "(methodCall <<foo>> <<bar>>)", "final"],
[["def <<foo>> <<params>> <<bar>>"], "(def <<foo>> <<params>> <<bar>>)", "final"],
[["[ <<foo>> ]"], "([ <<foo>> ])", "final"],
[["<<foo>> ,"], "<<foo>>,", "final"],
[["<<foo>> = <<bar>>"], "(setVar <<foo>> <<bar>>)", "final"],
]