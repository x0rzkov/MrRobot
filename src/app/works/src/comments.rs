use crate::{composer::steps, create_work, regex, Variable};

create_work!(comments; data, variables => {
    let src: String = steps::get_param("src", data, variables)?;
    let language_param: String = steps::get_param("language", data, variables)?;
    let languages: Vec<&str> = language_param.split(",").map(|lang| lang.trim()).collect();
    let mut result: String = String::new();
    for language in languages {
        let (re_line, re_multiline): (&str,&str) = match language.as_ref() {
            "css" |
            "js"  | "javascript" => (r"(^|\w)//[^\n]*",r"/\*[\s\S]*?\*/"),
            "html"               => (r"",r"<!--[\s\S]*?-->"),
            "web"                => (r"(^|\w)//[^\n]*",r"(/\*[\s\S]*?\*/|<!--[\s\S]*?-->)"),
            _ => (r"",r"")
        };
        let line: String = regex!(all; &src, re_line);
        let multiline: String = regex!(all; &src, re_multiline);
        result = [result,line,multiline].join("\n").trim().to_string();
    }
    Ok(Variable::Text(result))
});