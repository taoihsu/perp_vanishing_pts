function res = vanishing_lines_criteria(i,j,vp_1,lines,intn_pts,vote_matrix,~)
% This function returns true, if the points satisfy the vanishing lines
% criteria, (See Rother['02] for details). It also returns true if the
% vanishing line doesn't exist, i.e both the vanishing points are at Inf

% We define the thresholds here
a_thres = 5*pi/180;
d_thres = 30;

res1 = check_theshold_vlines(i,j,lines,intn_pts,vote_matrix,a_thres,d_thres);

res2 = check_theshold_vlines(i,vp_1,lines,intn_pts,vote_matrix,a_thres,d_thres);

res3 = check_theshold_vlines(j,vp_1,lines,intn_pts,vote_matrix,a_thres,d_thres);

res = res1&&res2&&res3;

%figure(2), hold off, imshow(1/5*grayIm)
%{
if (res == true)    
    figure(2), hold on, plot(lines(intn_pts(i,3:4),[1 2])',...
    lines(intn_pts(i,3:4),[3 4])','r')
    figure(2), hold on, plot(lines(intn_pts(j,3:4),[1 2])',...
    lines(intn_pts(j,3:4),[3 4])','b')
    figure(2), hold on, plot(lines(intn_pts(vp_1,3:4),[1 2])',...
    lines(intn_pts(vp_1,3:4),[3 4])','g')
    disp([i,j,vp_1])% checking purpose
    pause
end
%}
end

function res = check_theshold_vlines(i,j,lines,intn_pts,vote_matrix,a_thres,d_thres)
res = true;
% If either of the points are at Inf, then the criteria is satisied, if 
% both are at Inf, then the criteria doesn't apply thus we'll return the 
%min_angle possible.
if (intn_pts(i,2)==inf && intn_pts(j,2)==inf)    
    ang_line = atan((intn_pts(i,2)-intn_pts(j,2))/(intn_pts(i,1)-intn_pts(j,1)));
    com_lines = intersect(vote_matrix{i}{2},vote_matrix{j}{2});
    for l = com_lines
        p = abs(ang_line - lines(l,5));
        if(p>ang)
            ang = p;
        end
    end
elseif (intn_pts(i,2)==inf || intn_pts(j,2)==inf)
    if (intn_pts(i,2)==inf )
        x_inf = i; x_fin = j;
    else 
        x_inf = j; x_fin = i;
    end
    % Now let's estimate the angle and distance of each common line segment
    % from the vanishing line
    m_line = lines(x_inf,5);
else
end
end
